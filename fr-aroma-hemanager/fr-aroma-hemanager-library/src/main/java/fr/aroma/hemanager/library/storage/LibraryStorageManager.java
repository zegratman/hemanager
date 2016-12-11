/**
 * 
 */
package fr.aroma.hemanager.library.storage;

import java.util.List;

import fr.aroma.hemanager.library.data.HeItem;
import fr.aroma.hemanager.library.data.Library;

/**
 * Storage class for {@link Library} class.
 * @author mastering
 * @version $Id
 */
public interface LibraryStorageManager {
	
	/*--------> LIBRARY METHODS <---------*/
	
	/**
	 * Initialize a HE library with a given name.
	 * @param libraryName the library name.
	 * @throws LibraryStorageManagerException if the libraryName already exists.
	 */
	public void initLibrary(String libraryName) throws LibraryStorageManagerException;
	
	/*--------> HE METHODS <---------*/
	
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
	
	/**
	 * Get the list of HE identifiers available in the library.
	 * @param libraryName the library to search for.
	 * @return the list of available HE identifiers.
	 * @throws LibraryStorageManagerException if the library requested does not exist.
	 */
	public List<String> getHeIdentifiers(String libraryName) throws LibraryStorageManagerException;
	
	/**
	 * Method to update a HE identifier in the library.
	 * @param libraryName the library name.
	 * @param oldIdentifier the old identifier.
	 * @param newIdentifier the new identifier.
	 * @return true if the identifier is effectively updated.
	 * @throws LibraryStorageManagerException if the library name does not exist.
	 */
	public boolean updateHeIdentifier(String libraryName, String oldIdentifier, String newIdentifier) throws LibraryStorageManagerException;
	
	/**
	 * Get the HE usual names.
	 * @param libraryName the library name.
	 * @param heIdentifier the HE identifier.
	 * @return the list of usual names associated to the HE.
	 * @throws LibraryStorageManagerException if the library name does not exist.
	 */
	public List<String> getHeUsualNames(String libraryName, String heIdentifier) throws LibraryStorageManagerException;
	
	/**
	 * Method to add a HE usual name.
	 * @param libraryName the library name.
	 * @param heIdentifier the HE identifier.
	 * @param newUsualName the new usual name.
	 * @throws LibraryStorageManagerException if the library name does not exist.
	 */
	public void addHeUsualName(String libraryName, String heIdentifier, String newUsualName) throws LibraryStorageManagerException;
	
	/**
	 * Method to delete a usual name from a HE.
	 * @param libraryName the library name.
	 * @param heIdentifier the HE identifier.
	 * @param usualName the usual name to delete.
	 * @return true if the usual name was truly deleted.
	 * @throws LibraryStorageManagerException if the library name does not exists.
	 */
	public boolean deleteHeUsualName(String libraryName, String heIdentifier, String usualName) throws LibraryStorageManagerException;
	
	/**
	 * Get the HE identifiers corresponding to the given usual name.
	 * @param libraryName the library.
	 * @param usualName the usual name to use for search.
	 * @return the list of corresponding identifers.
	 * @throws LibraryStorageManagerException if the library name does not exist.
	 */
	public List<String> getHeIdentifersWithUsualName(String libraryName, String usualName) throws LibraryStorageManagerException;
	
	/*--------> TOXICITY METHODS <---------*/
	
	/**
	 * Method to create a new toxicity in the library
	 * @param library the library where to create the toxicity
	 * @param toxicityName the toxicity to add
	 * @throws LibraryStorageManagerException if the toxicity already exists
	 */
	public void createToxicity(String library, String toxicityName) throws LibraryStorageManagerException;
	
	/**
	 * Method to get the list of available toxicities in the library.
	 * @param library the library where to search for a toxicity.
	 * @return the list of available toxicities.
	 * @throws LibraryStorageManagerException if the requested library does not exist.
	 */
	public List<String> readToxicities(String library) throws LibraryStorageManagerException;
	
	/**
	 * Method to update a toxicity inside the library.
	 * @param library the library to use.
	 * @param oldToxicity the toxicity to update.
	 * @param newToxicity the new toxicity name.
	 * @return true if the toxicity was correctly updated.
	 * @throws LibraryStorageManagerException if the request library does not exist.
	 */
	public boolean updateToxicity(String library, String oldToxicity, String newToxicity) throws LibraryStorageManagerException;
	
	/**
	 * Method to delete a toxicity inside the library.
	 * @param library the library to use.
	 * @param toxicity the toxicity name to delete.
	 * @return true if the toxicity was correctly deleted.
	 * @throws LibraryStorageManagerException if the request library does not exist.
	 */
	public boolean deleteToxicity(String library, String toxicity) throws LibraryStorageManagerException;
	
}
