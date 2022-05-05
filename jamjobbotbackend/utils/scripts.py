import os

IMAGE_NAME = 'jamjobbotbackend'
# list of forwarded ports from host to conrainer in format <HostPort>:<ContainerPort>
FORWARDED_PORTS = [
    '443:443',
    '80:80',
    '88:88',
    '8443:8443',
    '5432:5432'
]


def build():
    os.system(f'docker build . -t {IMAGE_NAME}')


def dev():
    forwarded_ports = ''.join(map(lambda ports: f'-p {ports} ', FORWARDED_PORTS))
    build()
    os.system(f'docker run {forwarded_ports} --rm {IMAGE_NAME}')

