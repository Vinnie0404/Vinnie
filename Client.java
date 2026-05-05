
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);

            StringConcat stub = (StringConcat) registry.lookup("ConcatService");

            String result = stub.concatenate("Hello ", "World!");

            System.out.println("Concatenated String: " + result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
