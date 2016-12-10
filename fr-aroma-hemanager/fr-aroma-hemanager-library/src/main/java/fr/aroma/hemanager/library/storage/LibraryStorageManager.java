/**
 * 
 */
package fr.aroma.hemanager.library.storage;

import fr.aroma.hemanager.library.data.HeItem;
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
	
	/**
	 * Add a full HE into the library, this HE must NOT exist prior to this method call.
	 * @param libraryName the library name in which insert the HE
	 * @param heItem the HE to insert
	 * @throws LibraryStorageManagerException if an error occurs inserting the HE
	 */
	public void createHe(String libraryName, HeItem heItem) throws LibraryStorageManagerException;
	
	/**
	 * Get the HE according to the library and its latin name as identifier.
	 * @param libraryName the library name
	 * @param heItemIdentifier the HE identifier (latin name)
	 * @return the corresponding item
	 * @throws LibraryStorageManagerException if an error occurs retrieving the HE
	 */
	public HeItem readHe(String libraryName, String heItemIdentifier) throws LibraryStorageManagerException;
	
	/**
	 * Update an existing HE with a new instance.
	 * @param libraryName the library name.
	 * @param heItem the HE item to use for replace.
	 * @return true if the item has been successfully updated.
	 * @throws LibraryStorageManagerException if an error occurs during replace.
	 */
	public boolean updateHe(String libraryName, HeItem heItem) throws LibraryStorageManagerException;
	
	/**
	 * Delete a HE item into the library.
	 * @param libraryName the library name.
	 * @param heItem the HE item to delete.
	 * @return true if the item was successfully deleted.
	 * @throws LibraryStorageManagerException if an error occurs during deletion.
	 */
	public boolean deleteHe(String libraryName, HeItem heItem) throws LibraryStorageManagerException;
}
