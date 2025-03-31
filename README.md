# Examples
---
## Convert IP from decimal to binary
```bash
python3 ips.py -b 192.168.1.1
```

## Convert IP from binary to decimal
```bash
python3 ips.py -d 11000000.10101000.00000001.00000001
```

## Calculate network address from IP and subnet mask [ip/mask]
```bash
python3 ips.py -s 192.168.1.10/24
python3 ips.py -s 11000000.10101000.00000001.00001010/24
```

## Divide network into subnets with specific host size [ip/mask/host]
```bash
python3 ips.py -H 192.168.1.0/24/50
python3 ips.py -H 11000000.10101000.00000001.00000000/24/50
```

## Divide network into N equal subnets [ip/mask/subnets]
```bash
python3 ips.py -N 192.168.1.0/24/4
python3 ips.py -N 11000000.10101000.00000001.00000000/24/4
```

## Divide network using Variable Length Subnet Masking [ip/mask/hosts,hosts,...]
```bash
python3 ips.py -V 192.168.1.0/24/50,20,10
python3 ips.py -V 11000000.10101000.00000001.00000000/24/50,20,10
```
