import java.util.Calendar;

/**
 * Represents a Student.
 * 
 * @author sofos@aueb.gr
 *
 */
public class Student {

	private String name;
	private String surname;
	private int birthyear;
	private String am;

	/**
	 * Default constructor
	 * 
	 */
	public Student(){
	
	}

	/**
	 * Full constructor
	 * 
	 * @param am
	 *        Student's Registration number.
	 * @param name
	 *        Student's name.
	 * @param surname
	 *        Student's surname.
	 * @param birthyear
	 *        Student's year of birth.
	 */
	public Student(String am, String name, String surname, int birthyear) {

		this.am = am;
		this.name = name;
		this.surname = surname;
		this.birthyear = birthyear;

	}

	/**
	 * Sets Student's name
	 * 
	 * @param name
	 * 		  Student's name
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * A method to get Student's name.
	 * 
	 * @return Student's name
	 */
	public String getName() {
		return name;
	}

	/**
	 * Sets Student's surname
	 * 
	 * @param surname
	 *        Student's surname
	 */
	public void setSurname(String surname) {
		this.surname = surname;
	}

	/**
	 * A method to get Student's surname.
	 * 
	 * @return Student's surname
	 */
	public String getSurname() {
		return surname;
	}

	/**
	 * Sets Student's year of birth.
	 * 
	 * @param birthyear
	 *        Student's year of birth
	 */
	public void setBirthyear(int birthyear){
		this.birthyear = birthyear;
	}

	/**
	 * A method to get Student's year of birth.
	 * 
	 * @return Student's year of birth
	 */
	public int getBirthyear() {
		return birthyear;
	}

	/**
	 * Sets Student's registration number.
	 * 
	 * @param am
	 *        Student's registration number
	 */
	public void setAm(String am) {
		this.am = am;
	}

	/**
	 * A method to get Student's registration number.
	 * 
	 * @return Student's registration number
	 */
	public String getAm() {
		return am;
	}

	/**
	 * Returns Student's age.
	 * 
	 * @return Student's age
	 */
	public int getAge(){

		Calendar now = Calendar.getInstance();

		return now.get(Calendar.YEAR) - birthyear;
	}

	/**
	 * Customizing the inherited method.   
	 * 
	 */
	@Override
	public String toString() {

		String pdata = "----------------------" + "\n"
						+ "Student Personal Data:" + "\n"
						+ "----------------------" + "\n"
						+ "AM: " + am + "\n"
						+ "Name: " + name + "\n"
						+ "Surname: " + surname + "\n"
						+ "birthyear: " + birthyear + "\n"
						+ "Age: " + getAge();

		return pdata;
	}	
	
}//End of class
