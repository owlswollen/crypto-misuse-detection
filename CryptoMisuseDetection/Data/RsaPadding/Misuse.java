// RSA with no padding is insecure

class Misuse {
    Cipher.getInstance("RSA/NONE/NoPadding");
}