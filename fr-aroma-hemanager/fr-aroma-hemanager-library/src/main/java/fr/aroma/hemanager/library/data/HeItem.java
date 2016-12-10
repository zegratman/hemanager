/**
 * 
 */
package fr.aroma.hemanager.library.data;

import java.util.List;

/**
 * POJO class for he item
 * @author mastering
 * @version $Id
 */
public class HeItem {

	/**
	 * latin key name of the HE
	 */
	private String heLatinKey;
	
	/**
	 * usual names
	 */
	private List<String> usualNames;
	
	/**
	 * toxicities
	 */
	private List<String> toxicities;
	
	/**
	 * properties
	 */
	private List<HeProperty> properties;
	
	/**
	 * pathologies
	 */
	private List<HePathology> pathologies;
	
	/**
	 * descriptions
	 */
	private List<HeDescription> descriptions;
	
	/**
	 * prices
	 */
	private List<HePrice> prices;
	
	/**
	 * Constructor
	 */
	public HeItem() {
		
	}

	/**
	 * @return the heLatinKey
	 */
	public final String getHeLatinKey() {
		return heLatinKey;
	}

	/**
	 * @param heLatinKey the heLatinKey to set
	 */
	public final void setHeLatinKey(String heLatinKey) {
		this.heLatinKey = heLatinKey;
	}

	/**
	 * @return the usualNames
	 */
	public final List<String> getUsualNames() {
		return usualNames;
	}

	/**
	 * @param usualNames the usualNames to set
	 */
	public final void setUsualNames(List<String> usualNames) {
		this.usualNames = usualNames;
	}

	/**
	 * @return the toxicities
	 */
	public final List<String> getToxicities() {
		return toxicities;
	}

	/**
	 * @param toxicities the toxicities to set
	 */
	public final void setToxicities(List<String> toxicities) {
		this.toxicities = toxicities;
	}

	/**
	 * @return the properties
	 */
	public final List<HeProperty> getProperties() {
		return properties;
	}

	/**
	 * @param properties the properties to set
	 */
	public final void setProperties(List<HeProperty> properties) {
		this.properties = properties;
	}

	/**
	 * @return the pathologies
	 */
	public final List<HePathology> getPathologies() {
		return pathologies;
	}

	/**
	 * @param pathologies the pathologies to set
	 */
	public final void setPathologies(List<HePathology> pathologies) {
		this.pathologies = pathologies;
	}

	/**
	 * @return the descriptions
	 */
	public final List<HeDescription> getDescriptions() {
		return descriptions;
	}

	/**
	 * @param descriptions the descriptions to set
	 */
	public final void setDescriptions(List<HeDescription> descriptions) {
		this.descriptions = descriptions;
	}

	/**
	 * @return the prices
	 */
	public final List<HePrice> getPrices() {
		return prices;
	}

	/**
	 * @param prices the prices to set
	 */
	public final void setPrices(List<HePrice> prices) {
		this.prices = prices;
	}
	
}
