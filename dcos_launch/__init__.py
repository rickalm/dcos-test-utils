import dcos_launch.aws
import dcos_launch.arm
import dcos_launch.onprem
import dcos_launch.util
import dcos_launch.gce


def get_launcher(config):
    """Returns the correct class of launcher from a validated launch config dict
    """
    platform = config['platform']
    provider = config['provider']
    if platform == 'aws':
        if provider == 'aws':
            return dcos_launch.aws.DcosCloudformationLauncher(config)
        if provider == 'onprem':
            return dcos_launch.onprem.OnpremLauncher(config)
    if platform == 'azure':
        return dcos_launch.arm.AzureResourceGroupLauncher(config)
    if platform == 'gce':
        if provider == 'onprem':
            return dcos_launch.onprem.OnpremLauncher(config)
        else:
            raise dcos_launch.util.LauncherError('UnsupportedAction', 'Launch provider {} not supported for the {} platform.'.format(provider, platform))
    raise dcos_launch.util.LauncherError('UnsupportedAction', 'Launch platform not supported: {}'.format(platform))
