import aws_cdk as cdk
from aws_cdk import(
    Duration,
    RemovalPolicy,
    aws_backup as backup,
    aws_events as events,
    aws_kms as kms
)

from constructs import Construct

class Backup_Stack(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

                # ############### Backup Policies ###############

        # Create Backup Vault

        self.Backup_Vault=backup.BackupVault(
            self,
            "ASG_Backup_Vault",
            backup_vault_name="Backup_Vault",
            Vault_Key=kms.Key(
                self,  
                "Vault_Key",
                enable_key_rotation=True,
                alias="Vault_Key",
                removal_policy=RemovalPolicy.DESTROY
                ),
            removal_policy=RemovalPolicy.DESTROY
        )

        # Create Backup Plan

        self.Backup_Plan=backup.BackupPlan(
            self,
            "Backup_Plan",
            backup_vault=self.Backup_Vault
        )

        # # Add Resources to plan

        # ASGplan.add_selection("ASG",
        # resources=[
        #     backup.BackupResource.from_auto_scaling_group(ASG)
        # ]
        # )

        # Add Backup Rule: each day at 00:00 with 7 days retention

        self.Backup_Plan.add_rule(
            backup.BackupPlanRule(
                backup_vault=self.Backup_Vault,
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
