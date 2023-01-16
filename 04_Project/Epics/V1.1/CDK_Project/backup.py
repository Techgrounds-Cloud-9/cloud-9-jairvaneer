from aws_cdk import(
    Duration,
    RemovalPolicy,
    aws_backup as backup,
    aws_events as events,
    Tags
)

from constructs import Construct

class Backup_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, asg, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

                ############### Backup ###############

        # Create Tag

        Tags.of(asg).add("asg_tag", "asg_tag_value")

        # Create Backup Vault

        backup_vault=backup.BackupVault(
            self,
            "Backup_Vault",
            backup_vault_name="Backup_Vault",
            removal_policy=RemovalPolicy.DESTROY
        )

        # Create Backup Plan

        backup_plan=backup.BackupPlan(
            self,
            "backupplan",
            backup_vault=backup_vault
        )

        # # Add Resources to plan

        backup_plan.add_selection(
            "Selection",
            resources=[
                backup.BackupResource.from_tag("asg_tag", "asg_tag_value")
            ]
        )

        # Add Backup Rule: each day at 00:00 with 7 days retention

        backup_plan.add_rule(
            backup.BackupPlanRule(
                backup_vault=backup_vault,
                rule_name="Daily_Backup_7_Day_Retention",
                schedule_expression=events.Schedule.cron(
                    week_day="*",
                    hour="0",
                    minute="0"
                    ),
                delete_after=Duration.days(7),
            )
        )
