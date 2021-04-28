// SystemDefaultHttpClient, HttpClientBuilder, or HttpClients

class CorrectUse {
    HttpClient client = new SystemDefaultHttpClient();
    client = HttpClientBuilder.create().useSystemProperties().build();
    client = HttpClients.createSystem();
}