import argparse
import math

def convert_to_bin(ip: list[str]) -> str:
    return ".".join(f"{int(octet):08b}" for octet in ip)

def convert_to_dec(ip: list[str]) -> str:
    return ".".join(str(int(octet, 2)) for octet in ip)

def is_binary_ip(ip: str) -> bool:
    return all(all(c in "01" for c in part) and len(part) == 8 for part in ip.split("."))

def parse_ip(ip: str) -> tuple[list[str], str]:
    if is_binary_ip(ip):
        return convert_to_dec(ip.split(".")).split("."), "bin"
    return ip.split("."), "dec"

def find_subnet_mask(hosts: int) -> int:
    return 32 - math.ceil(math.log2(hosts + 2))

def calculate_vlsm_subnets(network_ip: str, total_mask: int, hosts_list: list[int]):
    ip_dec, format_type = parse_ip(network_ip)
    network_bin = "".join(f"{int(octet):08b}" for octet in ip_dec)

    print("\nVLSM Subnets:")

    sorted_hosts = sorted(hosts_list, reverse=True)
    current_subnet = int(network_bin, 2)

    for hosts in sorted_hosts:
        mask = find_subnet_mask(hosts)
        increment = 2 ** (32 - mask)

        if format_type == "bin":
            network_addr = ".".join([f"{(current_subnet >> (8 * i)) & 0xFF:08b}" for i in range(3, -1, -1)])
        else:
            network_addr = ".".join(str((current_subnet >> (8 * i)) & 0xFF) for i in range(3, -1, -1))

        print(f"Subnet: {network_addr}/{mask} (supports {2**(32 - mask) - 2} hosts)")
        current_subnet += increment

parser = argparse.ArgumentParser(prog='IP Calculator', description='Calculations on IPs')

parser.add_argument('-b', '--to-binary', help='Convert IP from decimal to binary', type=str)
parser.add_argument('-d', '--to-decimal', help='Convert IP from binary to decimal', type=str)
parser.add_argument('-s', '--subnets', help='Calculate network address from IP and subnet mask', type=str)
parser.add_argument('-H', '--hosts', help='Divide network into subnets with specific host size', type=str)
parser.add_argument('-N', '--num-subnets', help='Divide network into N equal subnets', type=str)
parser.add_argument('-V', '--vlsm', help='Divide network using Variable Length Subnet Masking', type=str)

args = parser.parse_args()

if args.to_binary:
    ip = args.to_binary.strip().split('.')
    print(convert_to_bin(ip))

elif args.to_decimal:
    ip = args.to_decimal.strip().split('.')
    print(convert_to_dec(ip))

elif args.subnets:
    try:
        ip, mask = args.subnets.split("/")
        print(f"NETWORK ADDR: {calculate_network_address(ip.strip(), mask.strip())}/{mask}")
    except ValueError:
        print("Invalid subnet format. Use IP/MASK (e.g., 192.168.1.10/24)")

elif args.vlsm:
    try:
        ip, mask, hosts_str = args.vlsm.split("/")
        hosts_list = list(map(int, hosts_str.split(",")))
        calculate_vlsm_subnets(ip.strip(), int(mask), hosts_list)
    except ValueError:
        print("Invalid format. Use: IP/MASK/HOST1,HOST2,HOST3 (e.g., 192.168.1.0/24/50,20,10)")
