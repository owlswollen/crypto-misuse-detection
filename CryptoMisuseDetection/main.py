import os
import re


def detect():
    data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Data")
    data_dirs = [data_dir for data_dir in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, data_dir))]
    report = "==========================================================================\n\n"

    # iterate over all data files
    for rule in data_dirs:
        report += "-Checking " + rule + " samples-\n\n"
        for file in os.listdir(os.path.join(data_path, rule)):
            filename = os.path.join(data_path, rule, file)
            report += os.path.join(rule, file) + ":\n"

            # read file content
            with open(filename, 'r') as input:
                content = input.read()
                result = check_rules(content)
                report += result if result != "" else "No issues found\n"
            report += "\n"
        report += "==========================================================================\n\n"

    outfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Report.txt")
    with open(outfile, "w") as outfile:
        outfile.write(report)
    print(report)


def check_rules(content):
    # cipher
    report = ""
    pattern = re.compile("CBC/PKCS5Padding")
    if len(pattern.findall(content)) >= 1:
        report += "Cipher is susceptible to Padding Oracle\n"

    # cipher integrity
    patterns = ["/CBC", "/OFB", "/CTR", "/ECB"]
    modes = []
    for idx, pattern in enumerate(patterns):
        re_pattern = re.compile(pattern)
        if len(re_pattern.findall(content)) >= 1:
            modes.append(patterns[idx].replace("/", ""))
    if len(modes) > 0:
        report += "Cipher with no integrity: "
    for idx, mode in enumerate(modes):
        report += mode
        if idx == len(modes) - 1:
            report += "\n"
        else:
            report += ", "

    # default HTTP client
    pattern = re.compile("new DefaultHttpClient\(")
    if len(pattern.findall(content)) >= 1:
        report += "DefaultHttpClient with default constructor is not compatible with TLS 1.2\n"

    # DES, DESede (triple DES)
    pattern_des = re.compile("DES/")
    pattern_desede = re.compile("DESede/")
    if len(pattern_des.findall(content)) >= 1:
        report += "DES is insecure\n"
    if len(pattern_desede.findall(content)) >= 1:
        report += "DESede is insecure\n"

    # ECB Mode
    pattern = re.compile("/ECB")
    if len(pattern.findall(content)) >= 1:
        report += "ECB mode is insecure\n"

    # hash
    patterns = ["\"MD2", "\"MD4", "\"MD5", "\"SHA1"]
    hash_functions = []
    for idx, pattern in enumerate(patterns):
        re_pattern = re.compile(pattern)
        if len(re_pattern.findall(content)) >= 1:
            hash_functions.append(patterns[idx].replace("\"", ""))
    if len(hash_functions) > 0:
        report += "Weak hash functions: "
    for idx, hash_function in enumerate(hash_functions):
        report += hash_function
        if idx == len(hash_functions) - 1:
            report += "\n"
        else:
            report += ", "

    # HostnameVerifier
    pattern = re.compile("HostnameVerifier")
    if len(pattern.findall(content)) >= 1:
        report += "HostnameVerifier that accept any signed certificates\n"

    # IV
    pattern_iv = re.compile("IvParameterSpec")
    pattern_required = re.compile("new SecureRandom\(")
    if len(pattern_iv.findall(content)) >= 1 and len(pattern_required.findall(content)) == 0:
        report += "Static IV\n"

    # MessageDigest
    pattern = re.compile("extends MessageDigest")
    if len(pattern.findall(content)) >= 1:
        report += "Message digest is custom\n"

    # NullCipher
    pattern = re.compile("new NullCipher\(")
    if len(pattern.findall(content)) >= 1:
        report += "NullCipher is insecure\n"

    # PRNG
    pattern = re.compile("new Random\(")
    if len(pattern.findall(content)) >= 1:
        report += "Predictable pseudorandom number generator\n"

    # RSA key
    pattern_rsa = re.compile("\"RSA")
    pattern_size = re.compile(".initialize\(512")
    if len(pattern_rsa.findall(content)) >= 1 and len(pattern_size.findall(content)) >= 1:
        report += "RSA usage with short key\n"

    # RSA padding
    pattern = re.compile("RSA/.*/NoPadding")
    if len(pattern.findall(content)) >= 1:
        report += "RSA with no padding is insecure\n"

    # ServerSocket
    pattern = re.compile("new ServerSocket\(")
    if len(pattern.findall(content)) >= 1:
        report += "Unencrypted Server Socket\n"

    # Socket
    pattern = re.compile("new Socket\(")
    if len(pattern.findall(content)) >= 1:
        report += "Unencrypted Socket\n"

    # SSLContext
    pattern = re.compile("SSLContext.getInstance\(\"SSL")
    if len(pattern.findall(content)) >= 1:
        report += "Weak SSLContext\n"

    # TrustManager that accept any certificates
    pattern_manager = re.compile("X509TrustManager")
    pattern_required = re.compile(".getTrustManagers\(")
    if len(pattern_manager.findall(content)) >= 1 and len(pattern_required.findall(content)) == 0:
        report += "TrustManager that accept any certificates\n"

    return report


if __name__ == '__main__':
    detect()
