import socket
import json
import base64
import logging

server_address = ('0.0.0.0', 6666)  # Pastikan port sesuai dengan yang digunakan server

def send_command(command_str=""):
    global server_address
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    logging.warning(f"connecting to {server_address}")
    try:
        logging.warning(f"sending message ")
        sock.sendall(command_str.encode())
        data_received = ""
        while True:
            data = sock.recv(16)
            if data:
                data_received += data.decode()
                if "\r\n\r\n" in data_received:
                    break
            else:
                break
        hasil = json.loads(data_received)
        logging.warning("data received from server:")
        return hasil
    except:
        logging.warning("error during data receiving")
        return False

def remote_list():
    command_str = "LIST"
    hasil = send_command(command_str)
    if hasil['status'] == 'OK':
        print("daftar file : ")
        for nmfile in hasil['data']:
            print(f"- {nmfile}")
        return True
    else:
        print("Gagal")
        return False

def remote_get(filename=""):
    command_str = f"GET {filename}"
    hasil = send_command(command_str)
    if hasil['status'] == 'OK':
        namafile = hasil['data_namafile']
        isifile = base64.b64decode(hasil['data_file'])
        with open(namafile, 'wb+') as fp:
            fp.write(isifile)
        return True
    else:
        print("Gagal")
        return False

def remote_upload(filename):
    try:
        with open(filename, 'rb') as fp:
            filecontent = base64.b64encode(fp.read()).decode('utf-8')
        command_str = f"UPLOAD {filename} {filecontent}"
        hasil = send_command(command_str)
        if hasil['status'] == 'OK':
            print(f"{filename} uploaded successfully")
            return True
        else:
            print("Gagal upload")
            return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def remote_delete(filename):
    command_str = f"DELETE {filename}"
    hasil = send_command(command_str)
    if hasil['status'] == 'OK':
        print(f"{filename} deleted successfully")
        return True
    else:
        print("Gagal delete")
        return False

if __name__ == '__main__':
    server_address = ('0.0.0.0', 6666)  # Pastikan port sesuai dengan yang digunakan server
    remote_list()
    remote_get('donalbebek.jpg')
    #remote_upload('newfile.txt')
    remote_delete('newfile.txt')
