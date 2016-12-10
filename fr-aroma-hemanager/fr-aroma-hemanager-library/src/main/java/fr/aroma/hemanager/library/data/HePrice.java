/**
 * 
 */
package fr.aroma.hemanager.library.data;

/**
 * POJO class to represent en HE price
 * @author mastering
 * @version $Id
 */
public class HePrice {

	/**
	 * Main part of the price
	 */
	private Integer mainPart;
	
	/**
	 * Cent part of the price
	 */
	private Integer centPart;
	
	/**
	 * Devise attached to the price
	 */
	private Devise devise;
	
	/**
	 * Source of the price
	 */
	private String source;
	
	public HePrice() {
		
	}
	
	public static enum Devise {
		EUR, // euros
		USD, // US dollars
		UKP  // UK pounds
	}

	/**
	 * @return the mainPart
	 */
	public final Integer getMainPart() {
		return mainPart;
	}

	/**
	 * @param mainPart the mainPart to set
	 */
	public final void setMainPart(Integer mainPart) {
		this.mainPart = mainPart;
	}

	/**
	 * @return the centPart
	 */
	public final Integer getCentPart() {
		return centPart;
	}

	/**
	 * @param centPart the centPart to set
	 */
	public final void setCentPart(Integer centPart) {
		this.centPart = centPart;
	}

	/**
	 * @return the devise
	 */
	public final Devise getDevise() {
		return devise;
	}

	/**
	 * @param devise the devise to set
	 */
	public final void setDevise(Devise devise) {
		this.devise = devise;
	}

	/**
	 * @return the source
	 */
	public String getSource() {
		return source;
	}

	/**
	 * @param source the source to set
	 */
	public void setSource(String source) {
		this.source = source;
	}
}
