/**
 * 
 */
package fr.aroma.hemanager.library.data;

/**
 * POJO class to describe pathology associated to a HE
 * @author mastering
 * @version $Id
 */
public class HePathology {
	
	/**
	 * Pathology name
	 */
	private String name;
	
	/**
	 * Pathology description
	 */
	private String description;
	
	public HePathology() {

	}

	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * @return the description
	 */
	public String getDescription() {
		return description;
	}

	/**
	 * @param description the description to set
	 */
	public void setDescription(String description) {
		this.description = description;
	}
	
}
