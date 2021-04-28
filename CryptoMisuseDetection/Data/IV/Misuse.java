// Static IV

class Misuse {
    private static byte[] IV = new byte[16] {(byte)0,(byte)1,(byte)2,[...]};

    public void encrypt(String message) throws Exception {

        IvParameterSpec ivSpec = new IvParameterSpec(IV);
    }
}