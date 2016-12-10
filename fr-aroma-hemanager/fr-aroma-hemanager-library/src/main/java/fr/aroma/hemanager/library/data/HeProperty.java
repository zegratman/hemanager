/**
 * 
 */
package fr.aroma.hemanager.library.data;

/**
 * POJO class to describe a HE property
 * @author mastering
 *
 */
public class HeProperty {

	/**
	 * Property name
	 */
	private String name;
	
	/**
	 * Property efficiency
	 */
	private Integer efficiency;
	
	/**
	 * Constructor
	 */
	public HeProperty() {
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
	 * @return the efficiency
	 */
	public Integer getEfficiency() {
		return efficiency;
	}

	/**
	 * @param efficiency the efficiency to set
	 */
	public void setEfficiency(Integer efficiency) {
		this.efficiency = efficiency;
	}
	
}
