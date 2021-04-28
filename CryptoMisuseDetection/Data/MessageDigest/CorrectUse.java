// Use approved algorithms

class CorrectUse {
    void messageDigest() {
        MessageDigest sha256Digest = MessageDigest.getInstance("SHA256");
        sha256Digest.update(password.getBytes());
    }
}