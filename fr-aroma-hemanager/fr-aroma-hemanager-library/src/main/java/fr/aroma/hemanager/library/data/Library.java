/**
 * 
 */
package fr.aroma.hemanager.library.data;

import java.util.List;

/**
 * Main POJO class for HE library
 * @author mastering
 * @version $Id
 */
public class Library {

	/**
	 * Collection of HE
	 */
	private List<HeItem> heItems;

	/**
	 * Collection of HV
	 */
	private List<HvItem> hvItems;
	
	/**
	 * Constructor
	 */
	public Library() {

	}

	/**
	 * @return the heItems
	 */
	public List<HeItem> getHeItems() {
		return heItems;
	}

	/**
	 * @param heItems the heItems to set
	 */
	public void setHeItems(List<HeItem> heItems) {
		this.heItems = heItems;
	}

	/**
	 * @return the hvItems
	 */
	public List<HvItem> getHvItems() {
		return hvItems;
	}

	/**
	 * @param hvItems the hvItems to set
	 */
	public void setHvItems(List<HvItem> hvItems) {
		this.hvItems = hvItems;
	}

}
