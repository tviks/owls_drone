# owls_warehouse_drone

## Ссылки 

-  [VIO](https://github.com/Auterion/VIO)
-  [librealsense_jetson](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_jetson.md)

## Отключение пароля администратора

    sudo visudo
    
добавляем в коней файла

    $USER ALL=(ALL) NOPASSWD: ALL
    
## Заметки

    <arg name="gcs_url" default="udp://0.0.0.0:14550@192.168.31.23:14550" />
    
udev

    sudo cp 99-px4fmu.rules /lib/udev/rules.d
