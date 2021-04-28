// Don't keep password in the source code

class CorrectUse {
    void password() {
        private String SECRET_PASSWORD;  // Load password from outside

        Properties props = new Properties();
        props.put(Context.SECURITY_CREDENTIALS, SECRET_PASSWORD);
    }
}