import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    zeikinn = launch_ros.actions.Node(
        package='mypkg',
        executable='zeikinn',
        )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([zeikinn, listener])
