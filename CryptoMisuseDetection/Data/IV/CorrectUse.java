// Use secure random

class CorrectUse {
    public void encrypt(String message) throws Exception {

        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);

        IvParameterSpec ivSpec = new IvParameterSpec(iv);
    }
}