import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class StringConcatImpl extends UnicastRemoteObject implements StringConcat {

    protected StringConcatImpl() throws RemoteException {
        super();
    }

    public String concatenate(String str1, String str2) throws RemoteException {
        return str1 + str2;
    }
}
