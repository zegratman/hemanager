/**
 * 
 */
package fr.aroma.hemanager.library.data;

/**
 * POJO class for HE description
 * @author mastering
 * @version $Id
 */
public class HeDescription {

	/**
	 * Description content
	 */
	private String content;
	
	/**
	 * Source of the description (e.g. web site)
	 */
	private String source;
	
	public HeDescription() {
		
	}

	/**
	 * @return the description
	 */
	public final String getDescription() {
		return content;
	}

	/**
	 * @param description the description to set
	 */
	public final void setDescription(String description) {
		this.content = description;
	}

	/**
	 * @return the source
	 */
	public final String getSource() {
		return source;
	}

	/**
	 * @param source the source to set
	 */
	public final void setSource(String source) {
		this.source = source;
	}
	
}
