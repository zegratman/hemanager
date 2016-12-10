/**
 * 
 */
package fr.aroma.hemanager.library.storage;

import fr.aroma.hemanager.library.data.Library;

/**
 * Storage class for {@link Library} class.
 * @author mastering
 * @version $Id
 */
public interface LibraryStorageManager {
	
	/**
	 * Initialize a HE library with a given name.
	 * @param libraryName the library name.
	 * @throws LibraryStorageManagerException if the libraryName already exists.
	 */
	public void initLibrary(String libraryName) throws LibraryStorageManagerException;

}
