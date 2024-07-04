"""Launch uv3_image_pub stereo left & right in a component container."""

import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.actions import LoadComposableNodes
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    """Generate launch description with multiple components."""
    left_params = [
        {"acquisition_role": "leader"},
        {"acquisition_frame_rate": 30.0},
        {"topic": "stereo/left"},
        {"device_sn": "FDS20110009"},
        {"pixel_format": 0x110000D},  # RG10
        #  {'pixel_format': 0x1080009},  # RG8
        {"image_encoding": "BAYER_RGGB16"},
    ]
    #  {'image_encoding': 'BAYER_RGGB8'}]
    #  {'image_encoding': 'RGB8'}]
    right_params = [
        # {'acquisition_role': 'follower'},
        {"acquisition_frame_rate": 10.0},
        {"topic": "stereo/right"},
        {"device_sn": "EBH24010025"},
        # {"pixel_format": 0x110000D},  # RG10
        #  {'pixel_format': 0x1080009},  # RG8
        # {"device_sn": "FDS20110008"},
        # {"image_encoding": "BAYER_RGGB16"},
    ]
    # {'image_encoding': 'BAYER_RGGB8'}]
    #  {'image_encoding': 'RGB8'}]

    container1 = ComposableNodeContainer(
        name="stereo_image_container",
        namespace="",
        package="rclcpp_components",
        executable="component_container_mt",
        composable_node_descriptions=[
            # ComposableNode(
            #   package='galaxy_camera_u3v',
            #   plugin='camera::U3vImagePub',
            #   name='left_image_pub',
            #   parameters=left_params
            # ),
            ComposableNode(
                package="galaxy_camera_u3v",
                plugin="camera::U3vImagePub",
                name="right_image_pub",
                parameters=right_params,
            )
        ],
    )

    return launch.LaunchDescription([container1])
