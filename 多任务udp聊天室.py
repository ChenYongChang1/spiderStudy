import socket
import threading


def recv_msg(udp_socket):
    '''接受数据显示'''
    # 接受数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_data(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input('请输入要发送的数据:')
        udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def main():
    '''
    完成udp聊天室的整体控制
    :return:
    '''
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地数据
    udp_socket.bind(('127.0.0.1', 1780))
    # 获取对方的ip
    dest_ip = input('请输入对方ip')
    dest_port = int(input('请输入对方port'))
    # 创建线程
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_data, args=(udp_socket, dest_ip, dest_port))
    t_recv.start()
    t_send.start()

if __name__ == '__main__':
    main()
