import pandas as pd
import csv

data = pd.read_csv('Car_Sales_Data_Set.csv',delimiter=',')
data.sort_values(["Country","Time_Year","Time_Quarter","Car_Manufacturer"],axis=0,ascending=True,inplace=True)
data = data.reset_index(drop=True)

for i in range(0,100,1):
    data = data.set_value(i,"Record_ID",i+1)

data.to_csv('Car_Sales_Data_Set_Sorted.csv',sep=',')

try:
    sorted_df = pd.read_csv('Car_Sales_Data_Set_Sorted.csv',delimiter=',')

    def one():
        print('')

    def two():

        new_df = sorted_df.groupby(['Country']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def three():
        new_df =sorted_df.groupby(['Time_Year']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def four():
        sorted_df['Time_Period'] = sorted_df['Time_Quarter'].map(str)+ '-'+ sorted_df['Time_Year'].map(str)
        new_df = sorted_df.groupby(['Time_Period']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def five():
        new_df =sorted_df.groupby(['Car_Manufacturer']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def six():
        new_df = sorted_df.groupby(['Country','Time_Year']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def seven():
        sorted_df['Time_Period'] = sorted_df['Time_Quarter'].map(str) + '-' + sorted_df['Time_Year'].map(str)
        new_df = sorted_df.groupby(['Country','Time_Period']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def eight():
        new_df = sorted_df.groupby(['Country','Car_Manufacturer']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def nine():
        new_df = sorted_df.groupby(['Time_Year','Car_Manufacturer']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def ten():
        sorted_df['Time_Period'] = sorted_df['Time_Quarter'].map(str) + '-' + sorted_df['Time_Year'].map(str)
        new_df = sorted_df.groupby(['Time_Period','Car_Manufacturer']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def eleven():
        new_df = sorted_df.groupby(['Country','Time_Year', 'Car_Manufacturer']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))

    def twelve():
        sorted_df['Time_Period'] = sorted_df['Time_Quarter'].map(str) + '-' + sorted_df['Time_Year'].map(str)
        new_df = sorted_df.groupby(['Country','Time_Period', 'Car_Manufacturer']).Sales_Units.sum().reset_index(name='Sales_Units')
        print(new_df.to_string(index=False))


    def Get_Data_Cube(argument):
        switcher = {
            1: one,
            2: two,
            3: three,
            4: four,
            5: five,
            6: six,
            7: seven,
            8: eight,
            9: nine,
            10: ten,
            11: eleven,
            12: twelve
        }
        funct = switcher.get(argument, lambda: "Invalid query number")
        print (funct())
    if __name__ == "__main__":

        argument = int(input("Please enter the number for query: "))
        Get_Data_Cube(argument)


except:
    print(Exception.__name__())




