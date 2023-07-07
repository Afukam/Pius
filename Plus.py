import subprocess
import argparse


def run_nmap(command, ip_address):
    full_command = ["nmap"] + command.split() + [ip_address]
    print(f"Running Nmap command: {full_command}")
    try:
        subprocess.call(full_command)
    except subprocess.CalledProcessError as e:
        print("[-] An error occurred while running nmap.")


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--command", dest="command", help="Nmap command to run")
    parser.add_argument("-i", "--ip", dest="ip_address", help="IP address to scan")
    options = parser.parse_args()

    if not options.command:
        parser.error("[-] Please specify the nmap command, use --help or -h for more information")

    if not options.ip_address:
        parser.error("[-] Please specify the IP address, use --help or -h for more information")

    return options


options = get_arguments()
run_nmap(options.command, options.ip_address)
