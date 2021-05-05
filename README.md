# owls_warehouse_drone

## Ссылки 

-  [VIO](https://github.com/Auterion/VIO)
-  [librealsense_jetson](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_jetson.md)

## Отключение пароля администратора

    sudo visudo
    
добавляем в коней файла

    root    ALL=(ALL:ALL) NOPASSWD: ALL
    
    owls    ALL=(ALL) NOPASSWD: ALL
    
## Swap resize 

[LINK](https://bogdancornianu.com/change-swap-size-in-ubuntu/)
    
## Заметки

    <arg name="gcs_url" default="udp://0.0.0.0:14550@192.168.31.23:14550" />
    
udev

    sudo cp 99-px4fmu.rules /lib/udev/rules.d
    
CUDA

    # cuda 10.2
    export CUDA_HOME=/usr/local/cuda
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64
    
slam error 

   [LINK](https://github.com/IntelRealSense/realsense-ros/issues/749#issuecomment-532968059)

system-throttled-due-to-over-current

   [LINK](https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3243/index.html#page/Tegra%2520Linux%2520Driver%2520Package%2520Development%2520Guide%2Fpower_management_nano.html%23wwpID0E0VD0HA)
