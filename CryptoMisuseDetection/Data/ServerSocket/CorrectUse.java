// SSL Server Socket

class CorrectUse {
    ServerSocket soc = SSLServerSocketFactory.getDefault().createServerSocket(1234);
}