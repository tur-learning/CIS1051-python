import argparse
import subprocess
from flask import Flask, send_file

# this is to feed the Flask app - serving turtle module output on the browser
output = "shape.svg"

app = Flask(__name__)

@app.route("/")
def main():
    subprocess.run(["python", "turtle_graphics.py", output])
    return send_file(output)

# if __name__ == "__main__":
#     app.run(host="172.17.0.4", port=8030)

if __name__ == "__main__":

    defaul_ip = subprocess.run(
                "ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                )

    if defaul_ip.returncode == 0:
        container_ip = defaul_ip.stdout.decode().strip()
        print(f"The container IP address is: {container_ip}")
    else:
        error = result.stderr.decode().strip()
        print(f"Error: {error}")

    default_port=8030

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default=container_ip, type=str, help="host address")
    parser.add_argument("--port", default=default_port, type=int, help="port number")
    args = parser.parse_args()
    app.run(host=args.host, port=args.port)