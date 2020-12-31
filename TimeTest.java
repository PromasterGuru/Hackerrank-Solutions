import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;
import java.util.TimeZone;

class TimeTest{

    public static Date parseShortDate(String dateTime) {
        try {
            SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yy", Locale.getDefault());
            formatter.setTimeZone(TimeZone.getDefault());
            return formatter.parse(dateTime);
        } catch (ParseException ignored) {}
        return null;
    }

    /**
     * Formats timestamp to 'date month' format (e.g. '3 Feb 2019'). //"dd-MM-yyyy"
     */
    public static String formatShortDate(String dateTime) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd MMM yyyy", Locale.getDefault());
        dateFormat.setTimeZone(TimeZone.getDefault());
        Date value = parseShortDate(dateTime);
        if (value == null){
            return null;
        }
        return dateFormat.format(value);
    }
    public static void main(String args[]){
        System.out.println("Dare: "+ formatShortDate("30/12/2020"));
        System.out.println("Dare: "+ formatShortDate("12/30/2020"));
    }
}