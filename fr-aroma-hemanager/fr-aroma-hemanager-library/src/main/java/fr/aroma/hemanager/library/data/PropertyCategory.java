/**
 * 
 */
package fr.aroma.hemanager.library.data;

import java.util.List;

/**
 * POJO class for HE property category
 * @author mastering
 * @since $Id
 */
public class PropertyCategory {

	/**
	 * Category name
	 */
	private String name;
	
	/**
	 * Property names
	 */
	private List<String> propertyNames;
	
	/**
	 * Constructor
	 */
	public PropertyCategory() {
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
	 * @return the propertyNames
	 */
	public List<String> getPropertyNames() {
		return propertyNames;
	}

	/**
	 * @param propertyNames the propertyNames to set
	 */
	public void setPropertyNames(List<String> propertyNames) {
		this.propertyNames = propertyNames;
	}

}
