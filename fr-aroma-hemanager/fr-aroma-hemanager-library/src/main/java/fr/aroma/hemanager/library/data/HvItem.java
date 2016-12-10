/**
 * 
 */
package fr.aroma.hemanager.library.data;

import java.util.List;

/**
 * POJO class to describe a HV
 * @author mastering
 * @version $Id
 */
public class HvItem {

	/**
	 * HV name
	 */
	private String name;
	
	/**
	 * Property categories associated
	 */
	private List<PropertyCategory> categories;
	
	/**
	 * Descriptions of the HV
	 */
	private List<HeDescription> descriptions;
	
	/**
	 * Prices
	 */
	private List<HePrice> prices;
	
	/**
	 * Constructor
	 */
	public HvItem() {
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
	 * @return the categories
	 */
	public List<PropertyCategory> getCategories() {
		return categories;
	}

	/**
	 * @param categories the categories to set
	 */
	public void setCategories(List<PropertyCategory> categories) {
		this.categories = categories;
	}

	/**
	 * @return the descriptions
	 */
	public List<HeDescription> getDescriptions() {
		return descriptions;
	}

	/**
	 * @param descriptions the descriptions to set
	 */
	public void setDescriptions(List<HeDescription> descriptions) {
		this.descriptions = descriptions;
	}

	/**
	 * @return the prices
	 */
	public List<HePrice> getPrices() {
		return prices;
	}

	/**
	 * @param prices the prices to set
	 */
	public void setPrices(List<HePrice> prices) {
		this.prices = prices;
	}

}
