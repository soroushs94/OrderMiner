from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from work_order_categorizer import WO_Categorizer
import Taxonomy as tx
import matplotlib.pyplot as plt
import seaborn as sns

# Only needed for access to command line arguments
import sys
import pandas as pd
from UI import Ui_mainWindow

class MyMainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.menubar.setStyleSheet("QMenuBar { background-color: #336699; color: white; }")
        self.setWindowTitle('Order Miner')
        self.setWindowIcon(QIcon('4647617.png'))


        #list of button names
        self.buttons = [button for button in self.findChildren(QPushButton)]

        # list of work center check box names
        self.wc_chk = []
        for i in range(self.layout_chk.count()):
            item = self.layout_chk.itemAt(i)
            if isinstance(item.widget(), QCheckBox):
                self.wc_chk.append(item.widget())

        self.df = pd.DataFrame()
        self.labour_df = pd.DataFrame()
        self.filtered_df = pd.DataFrame()
        self.report_df = pd.DataFrame()

        self.btnstyle ="""
        QPushButton {
            background-color: rgb(20, 152, 213);
            color: white;
            border-radius: 10px; /* Adjust the value to control corner radius */
            border: none;
            padding: 10px 20px; /* Adjust padding as needed */}

        QPushButton:hover {
            background-color: #2980b9; /* Change color on hover */
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.4); /* Add a shadow effect */}
        """
        self.btnimportinvoice.setStyleSheet(self.btnstyle)
        self.btnimportwo.setStyleSheet(self.btnstyle)
        self.btnfilter.setStyleSheet(self.btnstyle)
        self.btnreport.setStyleSheet(self.btnstyle)
        self.btnexport.setStyleSheet(self.btnstyle)

        self.btnimportwo.clicked.connect(self.import_func_wo)
        self.btnimportinvoice.clicked.connect(self.import_func_invoice)
        self.btnfilter.clicked.connect(self.filter)
        self.btnexport.clicked.connect(self.export)
        self.btnreport.clicked.connect(self.generate_report)

    def import_func_wo(self):
        self.reset_widgets()
        self.lblpath.setText('processing...')
        self.open_file_dialog(mode='wo')

    def import_func_invoice(self):
        self.open_file_dialog(mode='invoice')

    def open_file_dialog(self,mode):

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)",
                                                   options=options)
        if file_path:
            self.linepath.setText(file_path)
            if file_path[-4:] == '.csv':
                try:
                    if mode == 'wo':
                        self.df = pd.read_csv(file_path)
                        if ('wcName' in self.df.columns) & ('clean_desc' in self.df.columns) & ('Building Name' in self.df.columns):
                            categorizer = WO_Categorizer(self.df,'clean_desc')
                            self.df = categorizer.get_categorized_df()
                            self.lblpath.setText('Successfully imported the {} records '.format(self.df.shape[0]))
                            self.update_widgets(self.df)
                        else:
                            self.df = pd.DataFrame()
                            self.lblpath.setText('The file is not processed work order records.')

                    elif mode == 'invoice':
                        self.labour_df = pd.read_csv(file_path)
                        cols = ['Total Charged','Total Paid','SO#','BuildingCode','Hours']
                        check = all(column in self.labour_df.columns for column in cols)
                        if check:
                            self.lblcost.setText('Successfully imported {} invoices.'.format(self.labour_df.shape[0]))
                        else:
                            self.labour_df = pd.DataFrame()
                            self.lblcost.setText('The dataset should include Total Charged, Hours, SO#, and BuildingCode.')

                except Exception as e:
                    if mode == 'wo':
                        self.lblpath.setText("Error loading CSV file: {}".format(e))
                        self.lblpath.adjustSize()
                    elif mode == 'invoice':
                        self.lblcost.setText("Error loading CSV file: {}".format(e))
                        self.lblcost.adjustSize()
            else:
                if mode == 'wo':
                    self.lblpath.setText('The selected file is not CSV')
                    self.lblpath.adjustSize()
                elif mode == 'invoice':
                    self.lblcost.setText('The selected file is not CSV')
                    self.lblcost.adjustSize()

        else:
            self.lblpath.setText('No files imported yet.')

    def reset_widgets(self):

        for btn in self.buttons:
            btn.setChecked(False)
            if '|' in btn.text():
                name = btn.text().split('|')[0]
                btn.setText(name)
                btn.adjustSize()


        for chk in self.wc_chk:
            chk.setChecked(False)
            if '|' in chk.text():
                name = chk.text().split('|')[0]
                chk.setText(name)
                chk.adjustSize()

    def update_widgets(self,df):

        keys = tx.keys
        wc_counts = dict(df['wcName'].value_counts())

        #should be a separate function
        for button in self.buttons:
            if str(button.text()).lower() in keys:
                name = button.text() + '| ' + str(df[str(button.text()).lower()].sum())
                button.setText(name)
                button.adjustSize()

        #should be separate function
        # the dataset should have correct formats for work centers
        #unlike the buttons, here the first letter of WCs are capitalized
        for chk in self.wc_chk:
            name = chk.text()
            if name in wc_counts:
                name += '| ' + str(wc_counts[name])
                chk.setText(name)
                chk.adjustSize()

        #should be a separate function
        unassigned_rows = df.index[df[keys].sum(axis=1) == 0]
        status_count = df.loc[unassigned_rows,'clean_desc'].str.contains('mobile status').sum()
        self.btnmobile.setText('Mobile Status| '+str(status_count))
        non_classified = len(unassigned_rows) - status_count
        self.btnnone.setText('Non-classified| '+str(non_classified))

    def filter(self):
        if self.df.shape[0]<1:
            self.lblfilter.setText('No records are uploaded yet.')
        else:
            actions_issues = []
            systems = []
            WCs = []

            for button in self.buttons:
                if button.isChecked():
                    name = str(button.text()).lower().split('|')[0]
                    if name in tx.concept_taxonomy.keys():
                        systems.append(name)
                    else:
                        actions_issues.append(name)

            for box in self.wc_chk:
                if box.isChecked():
                    name = box.text().split('|')[0]
                    WCs.append(name)

            self.filtered_df = self.filter_df(actions_issues, systems, WCs)
            self.lblfilter.setText('{} records were extracted.'.format(self.filtered_df.shape[0]))

    def filter_df(self,actions_issues,systems,WCs):
        df = self.df
        if len(WCs)>0:
            df = df[df['wcName'].isin(WCs)]

        if len(actions_issues)>0:
            index = set()
            for i in actions_issues:
                index=index.union(set(df[df[i]==1].index))
            df = df.loc[list(index)]

        if len(systems)>0:
            index = set()
            for i in systems:
                index = index.union(set(df[df[i] == 1].index))
            df = df.loc[list(index)]
        return df

    def save_csv(self,df):

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv);;All Files (*)",
                                                        options=options)
        if file_path:
            try:
                df.to_csv(file_path, index=True)
            except Exception as e:
                self.lblReport('Cannot save the file. Memory access.')

    def export(self):

        if self.df.shape[0]<1:
            self.lblfilter.setText('No work order records are uploaded yet.')
        else:

            self.filter()
            if self.filtered_df.shape[0] < 1:
                print('No record passed the filter.')
            else:
                self.save_csv(self.filtered_df)
                self.lblfilter.setText('The filtered records are successfully exported.')

    def generate_report(self):

        if self.df.shape[0]<1:
            self.lblReport.setText('No work order records are uploaded yet.')

        elif self.labour_df.shape[0]<1:
            self.lblReport.setText('The billing data is not uploaded yet.')

        else:
            self.filter()

            if self.filtered_df.shape[0]<1:
                print('No record passed the filter.')

            else:

                KPIs = ['Number of Work Orders', 'Number of Billings', 'avg Billing per Work Order', 'Total Paid',
                              'Total Charged', 'Charged to Paid Ratio', 'avg Paid per Work Order',
                              'avg Paid per Billing', 'avg Charged per Work Order', 'avg Charged per Billing',
                              'Total Hours', 'avg Hours per Work Order', 'avg Hours per Billing']

                self.report_df = pd.DataFrame(columns=KPIs)

                idx = self.filtered_df['ServiceOrder']

                self.index_kpi(idx,'All Orders')

                for building in self.filtered_df['Building Name'].dropna().unique():
                    bdg_idx = self.filtered_df[self.filtered_df['Building Name'] == building]['ServiceOrder']
                    self.index_kpi(bdg_idx,building)

                for wc in self.filtered_df['wcName'].dropna().unique():
                    wc_idx = self.filtered_df[self.filtered_df['wcName']==wc]['ServiceOrder']
                    self.index_kpi(wc_idx, wc)

                self.save_files()

    def index_kpi(self, idx,idx_name):

        filtered_labour = self.labour_df[self.labour_df['SO#'].isin(idx)]
        total_res = filtered_labour[['Total Paid', 'Total Charged', 'Hours']].sum().round(1)

        row = {'Total Paid':total_res['Total Paid'],'Total Charged':total_res['Total Charged'],
              'Total Hours':total_res['Hours'],
               'Charged to Paid Ratio': (total_res['Total Charged'] / total_res['Total Paid']).round(2),
              'Number of Work Orders':len(idx),
               'Number of Billings':len(self.labour_df[self.labour_df['SO#'].isin(idx)]),
              'avg Billing per Work Order': round(len(filtered_labour) / len(idx),2),
              'avg Paid per Work Order': (filtered_labour['Total Paid'].sum()/len(idx)).round(2),
              'avg Charged per Work Order': (filtered_labour['Total Charged'].sum()/len(idx)).round(2),
              'avg Paid per Billing': round(filtered_labour['Total Paid'].mean(),2),
              'avg Charged per Billing': round(filtered_labour['Total Charged'].mean(),2),
              'avg Hours per Work Order': (filtered_labour['Hours'].sum()/len(idx)).round(2),
              'avg Hours per Billing': round(filtered_labour['Hours'].mean(),2)}

        row = pd.DataFrame(row,index=[idx_name])

        self.report_df = pd.concat([self.report_df, row])

    def save_files(self):

        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder', '.')

        if folder_path:

            try:

                all_orders = '{}/All_Orders.csv'.format(folder_path)
                self.report_df.loc['All Orders'].to_csv(all_orders,index=True)

                if self.chkBuilding.isChecked():
                    buildings = self.filtered_df['Building Name'].dropna().unique()
                    bdg_df = self.report_df.loc[buildings]
                    bdg_orders = '{}/Buildings Report.csv'.format(folder_path)
                    bdg_df.to_csv(bdg_orders)

                if self.chkWC.isChecked():
                    wcs = self.filtered_df['wcName'].dropna().unique()
                    wc_df = self.report_df.loc[wcs]
                    wc_orders = '{}/Work Centers Report.csv'.format(folder_path)
                    wc_df.to_csv(wc_orders)

                if self.chkPaid.isChecked():
                    idx = self.filtered_df['ServiceOrder']
                    paid_plot = self.labour_df[self.labour_df['SO#'].isin(idx)].loc[:,['Total Paid']].describe().drop('count')
                    self.save_displot('Total Paid',paid_plot,folder_path)

                if self.chkHours.isChecked():
                    idx = self.filtered_df['ServiceOrder']
                    paid_plot = self.labour_df[self.labour_df['SO#'].isin(idx)].loc[:,['Hours']].describe().drop('count')
                    self.save_displot('Hours',paid_plot,folder_path)

                if self.chkCharged.isChecked():
                    idx = self.filtered_df['ServiceOrder']
                    paid_plot = self.labour_df[self.labour_df['SO#'].isin(idx)].loc[:,['Total Charged']].describe().drop('count')
                    self.save_displot('Total Charged',paid_plot,folder_path)

                if self.chkTopPaid.isChecked():
                    buildings = self.filtered_df['Building Name'].dropna().unique()
                    bdg_paid = self.report_df.loc[buildings]
                    top_bdg_paid = bdg_paid.nlargest(10, 'Total Paid')
                    self.save_barplot('Total Paid', top_bdg_paid,folder_path)

                if self.chkTopCharged.isChecked():
                    buildings = self.filtered_df['Building Name'].dropna().unique()
                    bdg_paid = self.report_df.loc[buildings]
                    top_bdg_paid = bdg_paid.nlargest(10, 'Total Charged')
                    self.save_barplot('Total Charged', top_bdg_paid,folder_path)

                if self.chkTopHours.isChecked():
                    buildings = self.filtered_df['Building Name'].dropna().unique()
                    bdg_paid = self.report_df.loc[buildings]
                    top_bdg_paid = bdg_paid.nlargest(10, 'Total Hours')
                    self.save_barplot('Total Hours', top_bdg_paid,folder_path)


                # Save the DataFrame to the selected folder as a CSV file
                self.lblReport.setText('The reports are successfully generated.')
            except Exception as e:
                print('Error saving DataFrame: {}'.format(str(e)))

    def save_displot(self,column_name,df,path):


        plt.figure(figsize=(10, 6))
        sns.set_style("whitegrid")
        ax = sns.barplot(x=column_name, y=df.index, data=df, palette='viridis')
        print('good so far')
        plt.xlabel(column_name)
        plt.ylabel('Values')
        plt.title('Summary Statistics for {}'.format(column_name))
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        print('good so far')
        # Add numerical values completely outside the bars to the right
        for p in ax.patches:
            width = p.get_width()
            plt.text(width * 1.01, p.get_y() + p.get_height() / 2, '{:.2f}'.format(width), ha='left', va='center')
        print('good so far')
        # Set the x-axis limit to accommodate the numbers
        plt.xlim(0, df[column_name].max() * 1.1)
        print('good so far')
        plt.savefig('{}/{} Distribution.png'.format(path, column_name))
        print('good so far')

    def save_barplot(self,parameter_name, top_10_df, path):

        building_names = top_10_df.index
        total_paid_values = top_10_df[parameter_name]

        plt.figure(figsize=(10, 6))
        plt.bar(building_names, total_paid_values, color='skyblue')
        plt.xlabel('Building Names')
        plt.ylabel(parameter_name)  # Use the parameter name as the y-axis label
        plt.title('Top 10 Buildings by {}'.format(parameter_name))

        # Rotate x-axis labels for better readability (optional)
        plt.xticks(rotation=45, ha='right')

        # Save the plot as an image with the specified parameter name in the specified path

        plt.savefig('{}/Top 10 Buildings by {}.png'.format(path, parameter_name))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.showMaximized()
    sys.exit(app.exec_())

