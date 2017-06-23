package Group;
/**
 * Created by Jiao on 2017/4/3.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.net.URI;
import java.util.Hashtable;
import java.util.Iterator;


import org.apache.hadoop.conf.Configuration;

import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.fs.Path;

import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.Put;

public class Hw1Grp3 {
    public static void main(String[] args) throws IOException {
        //filename & group by
        String fileName = args[0].substring(2,args[0].length());
        String group =  args[1].split(":")[1];

        String[] attr3 =  args[2].split(":");
        String[] R_x = attr3[1].split(",");

        String command1=" ";
        String command2="22";

        for(int i=0;i<R_x.length;i++){
//            System.out.println("I see command1: "+R_x[i].substring(0,3));
            switch(R_x[i].substring(0,3)){
                case "cou":
                    break;
                case "avg":
                    command1=R_x[i];
                    System.out.println("Command1: "+command1);
                    break;
                case "max":
                    command2=R_x[i];
                    System.out.println("Command2: "+command2);
                default: break;
            }
        }

        //hadoop read file
        String file= "hdfs://192.168.0.104:9000//"+fileName;
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(URI.create(file), conf);
        Path path = new Path(file);
        FSDataInputStream in_stream = fs.open(path);
        BufferedReader in = new BufferedReader(new InputStreamReader(in_stream));
        String s;

        Hashtable<String, Hw1> htable = new Hashtable<String,Hw1>();
        while ((s=in.readLine())!=null ) {
            String[] words = s.split("\\|");
            //R=/hw1/lineitem.tbl groupby:R2 res:count,max(R5)
            String key = words[Integer.valueOf(group.substring(group.length()-1))];
            if(htable.containsKey(key)){
                Hw1 value=htable.get(key);
                value.count=value.count+1;
                // System.out.println("keySet:"+key+" "+value.count);
                if(command2!="22"){
                    double 	max_now=Double.valueOf(words[Integer.valueOf(command2.substring(command2.length()-2,command2.length()-1))]);
                    if(max_now>value.max ){
                        value.max=max_now;
                    }
                }
                if(command1!=" "){
                    double 	avg_now=Double.valueOf(words[Integer.valueOf(command1.substring(command1.length()-2,command1.length()-1))]);
                    value.avg=value.avg+avg_now;
                }
                htable.put(key, value);
            }else htable.put(key,new Hw1(1,0,0));

        }

        System.out.print("finish it !");
        System.out.println(htable.size());

        in.close();
        fs.close();

        //writeback to hbase
        Configuration HBASE_CONFIG = new Configuration();
        //HBASE_CONFIG.set("hbase.zookeeper.quorum", "192.168.0.104");

        String tableName = "Result";
        String family="res";
        HBaseAdmin hBaseAdmin = new HBaseAdmin(HBASE_CONFIG);

        if (hBaseAdmin.tableExists(tableName)) { //check
            hBaseAdmin.disableTable(tableName);
            hBaseAdmin.deleteTable(tableName);
            System.out.println(tableName + " is exist,detele....");
        }

        HTableDescriptor htd = new HTableDescriptor(TableName.valueOf(tableName));
        HColumnDescriptor cf= new HColumnDescriptor(family);
        htd.addFamily(cf);

        hBaseAdmin.createTable(htd);
        hBaseAdmin.close();
        HTable HBasetable = new HTable(HBASE_CONFIG,TableName.valueOf(tableName));
        //System.out.println(htable.size());
        Iterator<String> iterator0 = htable.keySet().iterator();
        while(iterator0.hasNext()){
            String key = (String)iterator0.next();
            Hw1 value0 = htable.get(key);
            value0.avg=value0.avg/value0.count;

            BigDecimal b   =   new  BigDecimal(value0.avg);
            value0.avg=   b.setScale(2, BigDecimal.ROUND_HALF_UP).doubleValue();
            htable.put(key, value0);
            Put put = new Put(String.valueOf(key).getBytes());

            put.add(family.getBytes(), "count".getBytes(), String.valueOf(value0.count).getBytes());
            if(command1!=" "){
                put.add(family.getBytes(), command1.getBytes(), String.valueOf(value0.avg).getBytes());
            }
            if( command2!="22"){
                put.add(family.getBytes(), command2.getBytes(), String.valueOf(value0.max).getBytes());
            }
            System.out.println("keySet:"+key+" "+value0.count+" "+value0.avg+" "+value0.max);
            HBasetable.put(put);
        }
        HBasetable.close();
        System.out.println("put successful!!!");
    }
}

class Hw1{
    public int count ;
    public double avg;
    public double max;

    public Hw1(int count,double avg,double max){
        this.count=count;
        this.avg=avg;
        this.max=max;
    }

    public int hashCode(){
        return (String.valueOf(count)+String.valueOf(avg)+String.valueOf(max)).hashCode();
    }

    public String toString(){
        return String.valueOf(count)+String.valueOf(avg)+String.valueOf(max);
    }
}