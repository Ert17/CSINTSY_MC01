import java.util.*;

public class Inputs {
	Viewer view;
	public int row, column, goldX, goldY;
	ArrayList <Integer> pitX = new ArrayList<Integer>();
	ArrayList <Integer> pitY = new ArrayList<Integer>();
	ArrayList <Integer> beaconX = new ArrayList<Integer>();
	ArrayList <Integer> beaconY = new ArrayList<Integer>();
	ArrayList <String> pit = new ArrayList<String>();

	public int getColumn()
	{
		return column;
	}

	public int getRow()
	{
		return row;
	}

	public ArrayList<Integer> getPitX()
	{
		return pitX;
	}

	public ArrayList<Integer> getPitY()
	{
		return pitY;
	}

	public ArrayList<Integer> getBeaconX()
	{
		return beaconX;
	}

	public ArrayList<Integer> getBeaconY()
	{
		return beaconY;
	}

	public ArrayList<String> getPit()
	{
		return pit;
	}

	public int getGoldX()
	{
		return goldX;
	}

	public int getGoldY()

	{
		return goldY;
	}

	public void setColumn(int column)
	{
		this.column = column;
	}

	public void setRow(int row)
	{
		this.row = row;
	}

	public void setGoldX(int x)
	{
		goldX = x;
	}

	public void setGoldY(int y)
	{
		goldY = y;
	}

	public void addPitX(int x)
	{
		pitX.add(x);
	}

	public void addPitY(int y)
	{
		pitY.add(y);
	}

	public void addBeaconX(int x)
	{
		beaconX.add(x);
	}

	public void addBeaconY(int y)
	{
		beaconY.add(y);
	}

	public Inputs()
	{
		view = new Viewer(this);
	}

	public void clear()
	{
		for (int i = 0; i < pitX.size(); i++)
		{
			pitX.remove(i);
			pitY.remove(i);
		}

		for (int i = 0; i < beaconX.size(); i++)
		{
			beaconX.remove(i);
			beaconY.remove(i);
		}

		setGoldX(getColumn() - 1);
		setGoldY(getRow() - 1);
	}
}
