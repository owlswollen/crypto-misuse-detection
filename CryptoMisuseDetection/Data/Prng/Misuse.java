// Predictable pseudorandom number generator

class Misuse {
    public String generateSecretToken() {
        Random r = new Random();
        return Long.toHexString(r.nextLong());
    }
}