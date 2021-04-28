// MD2, MD4, MD5, and SHA-1 are weak hash functions

class Misuse {
    MessageDigest md5Digest = MessageDigest.getInstance("MD5");
    md5Digest.update(password.getBytes());
    byte[] hashValue = md5Digest.digest();

    MessageDigest md4Digest = MessageDigest.getInstance("MD4");
    md4Digest.update(password.getBytes());
    hashValue = md4Digest.digest();

    MessageDigest md2Digest = MessageDigest.getInstance("MD2");
    md2Digest.update(password.getBytes());
    hashValue = md2Digest.digest();

    MessageDigest sha1Digest = MessageDigest.getInstance("SHA1");
    sha1Digest.update(password.getBytes());
    byte[] hashValue = sha1Digest.digest();
}