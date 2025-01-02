import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    zeikinn = launch_ros.actions.Node(
        package='mypkg',
        executable='zeikinn',
        )
    rekishi = launch_ros.actions.Node(
        package='mypkg',
        executable='rekishi',
        output='screen'
        )

    return launch.LaunchDescription([zeikinn, rekishi])
