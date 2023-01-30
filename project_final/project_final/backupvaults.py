from aws_cdk import (
    Stack,
    Duration,
    RemovalPolicy,
    aws_backup as backup,
    aws_events as events,
    aws_ec2 as ec2
)

from constructs import Construct

class Backup_Construct(Stack):

    def __init__(self, scope: Construct, construct_id: str, instances: ec2.Instance, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ###### Backup Vaults ######
        Web_backup_vault = backup.BackupVault(
            self, 'Web_backup_vault',
            backup_vault_name='Webbackupvault',
            removal_policy=RemovalPolicy.DESTROY,
        )

        # Admin_backup_vault = backup.BackupVault(
        #     self, 'Admin backup vault',
        #     backup_vault_name='Admin backup-vault',
        #     removal_policy=RemovalPolicy.DESTROY,
        # )

        ###### Backup Plans ######
        Web_backup_plan = backup.BackupPlan(
            self, 'Web backup plan',
            backup_vault=Web_backup_vault,
        )

        # Admin_backup_plan = backup.BackupPlan(
        #     self, 'Admin backup plan',
        #     backup_vault=Admin_backup_vault,
        # )

        ###### Backup linked to Instances ######
        Web_backup_plan.add_selection(
            'Selection',
            resources=[backup.BackupResource.from_ec2_instance(instances)],
            allow_restores=True
        )

        # Admin_backup_plan.add_selection(
        #     'Plan selection',
        #     resources=[backup.BackupResource.from_ec2_instance(stay_connected)],
        #     allow_restores=True,
        # )   

        ###### Add Backup Rules ######
        Web_backup_plan.add_rule(backup.BackupPlanRule(
            schedule_expression=events.Schedule.cron(
                week_day='*',
                hour='17',
                minute='0'),
                enable_continuous_backup=True,
                delete_after=Duration.days(7),
            )
        )

        # Admin_backup_plan.add_rule(backup.BackupPlanRule(
        #     schedule_expression=events.Schedule.cron(
        #         week_day= '1',
        #         hour= '17',
        #         minute= '0'),
        #         enable_continuous_backup=True,
        #         delete_after=Duration.days(8),
        #     )
        # )