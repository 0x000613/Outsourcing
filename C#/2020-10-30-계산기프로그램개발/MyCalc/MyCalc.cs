using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyCalc
{
    public partial class MyCalc : Form
    {
        public MyCalc()
        {
            InitializeComponent();

            this.bnt_C_Click(this.bnt_C, null);
        }

        /// <summary>
        /// 숫자버튼 클릭
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void bnt_number_Click(object sender, EventArgs e)
        {
            Button _Button;

            _Button = (Button)sender;

            this.txt_Result.Text += _Button.Text;
        }

        /// <summary>
        /// 소수점 클릭
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void bnt_Point_Click(object sender, EventArgs e)
        {
            Button _Button;

            _Button = (Button)sender;

            if (!this.txt_Result.Text.Contains("."))
                this.txt_Result.Text += _Button.Text;
        }

        private decimal FirstValue;
        private string Operation;

        /// <summary>
        /// Operation 클릭
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void bnt_Operation_Click(object sender, EventArgs e)
        {
            Button _Button;

            if (this.txt_Result.Text == string.Empty)
                return;

            _Button = (Button)sender;

            this.Operation = _Button.Text;

            this.FirstValue = decimal.Parse(this.txt_Result.Text);

            this.txt_Result.Text = string.Empty;
        }

        /// <summary>
        /// Equal 클릭
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void bnt_Equal_Click(object sender, EventArgs e)
        {
            if (this.FirstValue == decimal.MinValue)
                return;

            if (this.Operation == string.Empty)
                return;

            if (this.txt_Result.Text == string.Empty)
                return;

            switch (this.Operation)
            {
                case "+":
                    this.txt_Result.Text = (this.FirstValue + decimal.Parse(this.txt_Result.Text)).ToString();
                    break;
                case "-":
                    this.txt_Result.Text = (this.FirstValue - decimal.Parse(this.txt_Result.Text)).ToString();
                    break;
                case "*":
                    this.txt_Result.Text = (this.FirstValue * decimal.Parse(this.txt_Result.Text)).ToString();
                    break;
                case "/":
                    if (this.txt_Result.Text == "0")
                        return;

                    this.txt_Result.Text = (this.FirstValue / decimal.Parse(this.txt_Result.Text)).ToString();
                    break;
            }
        }

        /// <summary>
        /// Clear 버튼
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void bnt_C_Click(object sender, EventArgs e)
        {
            this.FirstValue = decimal.MinValue;
            this.txt_Result.Text = string.Empty;
        }

        /// <summary>
        /// Back 클릭
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void bnt_Back_Click(object sender, EventArgs e)
        {
            if (this.txt_Result.Text == string.Empty)
                return;

            this.txt_Result.Text = this.txt_Result.Text.Substring(0, this.txt_Result.Text.Length - 1);
        }
    }
}