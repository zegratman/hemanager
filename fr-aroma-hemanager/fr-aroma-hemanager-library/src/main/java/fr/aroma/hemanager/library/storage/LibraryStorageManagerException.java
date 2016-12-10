/**
 * 
 */
package fr.aroma.hemanager.library.storage;

/**
 * Exception class
 * @author mastering
 * @version $Id
 */
public class LibraryStorageManagerException extends Throwable {

	/**
	 * Serial
	 */
	private static final long serialVersionUID = -948558451439193752L;
	
	public LibraryStorageManagerException() {
		super();
	}
	
	public LibraryStorageManagerException(String message) {
		super(message);
	}

	public LibraryStorageManagerException(String message, Throwable t) {
		super(message, t);
	}
	
	public LibraryStorageManagerException(Throwable t) {
		super(t);
	}
	
}
