import aws_cdk as cdk
from aws_cdk import(
    Duration,
    RemovalPolicy,
    aws_backup as backup,
    aws_events as events,
    aws_kms as kms,
    aws_autoscaling as autoscaling,
    Tags
)

from constructs import Construct

class Backup_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, autoscalinggroup: list, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        asg=autoscaling.AutoScalingGroup(self, "asg")

        # Create Tag

        Tags.of(asg).add("asg_tag", "asg_tag_value")

                ############### Backup Policies ###############

        # Create Vault Key

        vaultkey=kms.Key(
            self,  
            "Vault_Key",
            enable_key_rotation=True,
            alias="Vault_Key",
            removal_policy=RemovalPolicy.DESTROY
            ),

        # Create Backup Vault

        self.backup_vault=backup.BackupVault(
            self,
            "ASG_Backup_Vault",
            backup_vault_name="Backup_Vault",
            encryption_key=vaultkey,
            removal_policy=RemovalPolicy.DESTROY
        )

        # Create Backup Plan

        backupplan=backup.BackupPlan(
            self,
            "backupplan",
            backup_vault=self.backup_vault
        )

        # Add Resources to plan

        backupplan.add_selection(
            "Selection",
            resources=[
                backup.BackupResource.from_tag("asg_tag", "asg_tag_value")
            ]
        )

        # Add Backup Rule: each day at 00:00 with 7 days retention

        backupplan.add_rule(
            backup.BackupPlanRule(
                backup_vault=self.backup_vault,
                rule_name="Daily_Backup_7_Day_Retention",
                schedule_expression=events.Schedule.cron(
                    week_day="*",
                    hour="0",
                    minute="0"
                    ),
                delete_after=Duration.days(7),
            )
        )

        # recovery point time 24 hours
        # recovery speed ASAP