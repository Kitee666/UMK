#pragma checksum "..\..\EdycjaTermin.xaml" "{8829d00f-11b8-4213-878b-770e8597ac16}" "6308A13BEFD654415DDD048836C3BE4B0F508C09AEB2166A508A8DCC1520288A"
//------------------------------------------------------------------------------
// <auto-generated>
//     Ten kod został wygenerowany przez narzędzie.
//     Wersja wykonawcza:4.0.30319.42000
//
//     Zmiany w tym pliku mogą spowodować nieprawidłowe zachowanie i zostaną utracone, jeśli
//     kod zostanie ponownie wygenerowany.
// </auto-generated>
//------------------------------------------------------------------------------

using Plan;
using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Media.Media3D;
using System.Windows.Media.TextFormatting;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Shell;


namespace Plan {
    
    
    /// <summary>
    /// EdycjaTermin
    /// </summary>
    public partial class EdycjaTermin : System.Windows.Window, System.Windows.Markup.IComponentConnector {
        
        
        #line 24 "..\..\EdycjaTermin.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.TextBlock napis;
        
        #line default
        #line hidden
        
        
        #line 28 "..\..\EdycjaTermin.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.DatePicker Data;
        
        #line default
        #line hidden
        
        
        #line 29 "..\..\EdycjaTermin.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button Insert;
        
        #line default
        #line hidden
        
        
        #line 30 "..\..\EdycjaTermin.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button Update;
        
        #line default
        #line hidden
        
        
        #line 31 "..\..\EdycjaTermin.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button Delete;
        
        #line default
        #line hidden
        
        
        #line 34 "..\..\EdycjaTermin.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.DataGrid Dane;
        
        #line default
        #line hidden
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Uri resourceLocater = new System.Uri("/Plan;component/edycjatermin.xaml", System.UriKind.Relative);
            
            #line 1 "..\..\EdycjaTermin.xaml"
            System.Windows.Application.LoadComponent(this, resourceLocater);
            
            #line default
            #line hidden
        }
        
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Never)]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Design", "CA1033:InterfaceMethodsShouldBeCallableByChildTypes")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Maintainability", "CA1502:AvoidExcessiveComplexity")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1800:DoNotCastUnnecessarily")]
        void System.Windows.Markup.IComponentConnector.Connect(int connectionId, object target) {
            switch (connectionId)
            {
            case 1:
            this.napis = ((System.Windows.Controls.TextBlock)(target));
            return;
            case 2:
            this.Data = ((System.Windows.Controls.DatePicker)(target));
            return;
            case 3:
            this.Insert = ((System.Windows.Controls.Button)(target));
            
            #line 29 "..\..\EdycjaTermin.xaml"
            this.Insert.Click += new System.Windows.RoutedEventHandler(this.Dodaj);
            
            #line default
            #line hidden
            return;
            case 4:
            this.Update = ((System.Windows.Controls.Button)(target));
            
            #line 30 "..\..\EdycjaTermin.xaml"
            this.Update.Click += new System.Windows.RoutedEventHandler(this.Zmien);
            
            #line default
            #line hidden
            return;
            case 5:
            this.Delete = ((System.Windows.Controls.Button)(target));
            
            #line 31 "..\..\EdycjaTermin.xaml"
            this.Delete.Click += new System.Windows.RoutedEventHandler(this.Usun);
            
            #line default
            #line hidden
            return;
            case 6:
            
            #line 32 "..\..\EdycjaTermin.xaml"
            ((System.Windows.Controls.Button)(target)).Click += new System.Windows.RoutedEventHandler(this.Wyczysc);
            
            #line default
            #line hidden
            return;
            case 7:
            this.Dane = ((System.Windows.Controls.DataGrid)(target));
            
            #line 34 "..\..\EdycjaTermin.xaml"
            this.Dane.AutoGeneratingColumn += new System.EventHandler<System.Windows.Controls.DataGridAutoGeneratingColumnEventArgs>(this.Ukrywanie);
            
            #line default
            #line hidden
            
            #line 34 "..\..\EdycjaTermin.xaml"
            this.Dane.SelectionChanged += new System.Windows.Controls.SelectionChangedEventHandler(this.Wybrano);
            
            #line default
            #line hidden
            return;
            }
            this._contentLoaded = true;
        }
    }
}

