import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.awt.Point;

class Day2
{
    public static void main(String[] args)
    {
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        int[][] grid = new int[][] {{1,2,3},{4,5,6},{7,8,9}};

        //0 through 2 bounding
        Point pos = new Point(1,1);

        File file = new File("input.txt");
        BufferedReader br;
        try {
            br = new BufferedReader(new FileReader(file));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }

        String st;
        try {
            while ((st = br.readLine()) != null)
            {
                for (int i = 0; i < st.length(); i++)
                {
                    char direction = st.charAt(i);
                    pos = MovePoint(pos,direction);
                    pos = fixBounds(pos);
                }

                numbers.add(grid[pos.x][pos.y]);
            }
        } catch (IOException e) {
            System.err.println("Read Fail");
            return;
        }
        try {
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        String listString = "";

        for (int s : numbers)
        {
            listString += "" + s;
        }
        System.out.println(listString);
    }

    public static Point fixBounds(Point pos)
    {
        if(pos.x < 0)
        {
            return new Point(0,pos.y);
        }
        if(pos.x > 2)
        {
            return new Point(2,pos.y);
        }
        if(pos.y < 0)
        {
            return new Point(pos.x,0);
        }
        if(pos.y > 2)
        {
            return new Point(pos.x,2);
        }
        return pos;
    }

    public static Point MovePoint(Point pos,char direction)
    {
        Point newPos = new Point(pos.x,pos.y);
        
        if(direction == 'U')
        {
            newPos = new Point(pos.x,pos.y-1);
        }
        else if(direction == 'D')
        {
            newPos = new Point(pos.x,pos.y+1);
        }
        else if(direction == 'L')
        {
            newPos = new Point(pos.x-1,pos.y);
        }
        else if(direction == 'R')
        {
            newPos = new Point(pos.x+1,pos.y);
        }
        return newPos;
    }
}