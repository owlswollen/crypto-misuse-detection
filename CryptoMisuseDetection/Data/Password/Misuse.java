// Hard coded password

class Misuse {
    void password() {
        private String SECRET_PASSWORD = "letMeIn!";

        Properties props = new Properties();
        props.put(Context.SECURITY_CREDENTIALS, SECRET_PASSWORD);
        props.put(Context.SECURITY_CREDENTIALS, "p@ssw0rd");
    }
}