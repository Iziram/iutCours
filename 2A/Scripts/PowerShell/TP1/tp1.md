**BUT2 R&T - Module Script – Powershell - IUT Lannion**

**TP1 (2H) - Introduction au terminal PowerShell et manipulation des objets avec des cmd-lets**

***Vous devrez rendre un compte-rendu à chaque fin de TP, avec les lignes de commandes ainsi que les preuves de fonctionnement.***

Au cours de ce premier TP, nous allons découvrir l’utilisation du terminal de Powershell. Soyez curieux et naviguez dans l’aide (`cmd-let Get-Help`) pour compléter les manipulations suggérées ci-dessous :

# 1. Naviguer dans l’arborescence

* Créez un dossier `PowerShell` dans votre répertoire personnel, puis un dossier `TP1` dans le
dossier `PowerShell` nouvellement créé,
* Trouvez la `cmd-let` qui vous permettra de vous déplacer dans `PowerShell/TP1` (la `cmd-let get-alias` permettant de lister les alias),

  ```powershell
  Set-Location .\PowerShell\TP1\
  ```

* Trouvez et utilisez la `cmd-let` permettant de lister le contenu du dossier.

  ```powershell
  Get-ChildItem
  ```

  **Résultat**  

  ```txt
  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  -a----        28/02/2023     13:36           8630 tp1.md
  ```

# 2. Exécution de cmd-lets

* affichez l’aide en ligne et trouver le nom de la `cmd-let` qui vous permet d’obtenir la liste des cmd-lets disponibles,

  ```powershell
  Get-Command
  ```

  **Résultat**

  ```txt
    Function        Invoke-Pester                                      3.4.0      Pester
  Function        Invoke-Plaster                                     1.1.3      Plaster
  Function        It                                                 3.4.0      Pester
  Function        J:
  Function        Join-ScriptExtent                                  0.2.0      PowerShellEditorServices.Commands
  Function        K:
  Function        L:
  Function        Lock-BitLocker                                     1.0.0.0    BitLocker
  Function        M:
  Function        mkdir
  Function        Mock                                               3.4.0      Pester
  Function        more
  Function        Mount-DiskImage                                    2.0.0.0    Storage
  Function        Move-SmbWitnessClient                              2.0.0.0    SmbWitness
  Function        N:
  
  ...

  ```

* utilisez la `cmd-let` appropriée pour créer un élément du système de fichier de type File et de nom `introPowershell.md`,

  ```powershell
  New-Item introPowershell.md
  ```

  **Résultat**

  ```txt
  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  -a----        28/02/2023     13:44              0 introPowershell.md
  ```

* utilisez la `cmd-let` appropriée pour renommer le fichier `introPowershell.md` en `CR_TP1_Powershell.md`,

  ```powershell
  Move-Item introPowershell.md CR_TP1_Powershell.md
  # ou 
  Rename-Item introPowershell.md CR_TP1_Powershell.md
  ```

* utilisez la `cmd-let` appropriée pour ouvrir le document que vous venez de renommer.

  ```powershell
  Invoke-Item CR_TP1_Powershell.md
  ```

# 3. Manipuler des variables

* Déclarez une variable nommé **bonjour** contenant le texte suivant « Salut toi !»,

  ```powershell
  [String]$bonjour = "Salut toi !"
  ```

* Affichez le contenu de la variable **bonjour**,

  ```powershell
  Write-Output $bonjour
  ```

  **Résultat**

  ```txt
  Name                           Value
  ----                           -----
  bonjour                        Salut Toi!
  ```

* déclarez une variable **mesInterfaces** contenant les informations de vos interfaces réseaux (commande ipconfig) et affichez ce qu’elle contient. Comment éditez le type de la variable mesInterfaces ? Quel est-il ?

  ```powershell
  $mesInterfaces = ipconfig
  $mesInterfaces.GetType()
  
  ```

  **Résultat**

  ```txt
  IsPublic IsSerial Name                                     BaseType
  -------- -------- ----                                     --------
  True     True     Object[]                                 System.Array
  ```

  > Le retour est de type array (StringArray plus particulièrement)

* La `cmd-let` **get-variable** vous permet de voir la liste des variables accessibles. En vous appuyant sur l’aide, affichez toutes les variables commençant par PS,

  ```powershell
  Get-Variable PS*
  ```

  **Résultat**

  ```txt
  Name                           Value
  ----                           -----
  PSBoundParameters              {}
  PSCommandPath
  PSCulture                      fr-FR
  PSDefaultParameterValues       {}
  PSEdition                      Desktop
  psEditor                       Microsoft.PowerShell.EditorServices.Extensions.EditorObject
  PSEmailServer
  PSHOME                         C:\Windows\System32\WindowsPowerShell\v1.0
  PSScriptRoot
  PSSessionApplicationName       wsman
  PSSessionConfigurationName     http://schemas.microsoft.com/powershell/Microsoft.PowerShell
  PSSessionOption                System.Management.Automation.Remoting.PSSessionOption
  PSUICulture                    fr-FR
  PSVersionTable                 {PSVersion, PSEdition, PSCompatibleVersions, BuildVersion...}
  ```

* Toujours en utilisant la commande cmd-let `get-variable` [ou la commande équivalente `Get-ChildItem variable:` ] retrouvez des variables pré-définies que vous avez déjà utilisé sous Unix,

  ```txt
  PWD                            C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts
  HOME                           C:\Users\Matthias
  ```

* Étudiez les variables d’environnement à l’aide de la commande `Get-ChildItem env:`,

  ```txt
  Name                           Value                                                                                                     
  ----                           -----                                                                                                     
  ALLUSERSPROFILE                C:\ProgramData                                                                                            
  APPDATA                        C:\Users\Matthias\AppData\Roaming                                                                         
  ChocolateyInstall              C:\ProgramData\chocolatey                                                                                 
  ChocolateyLastPathUpdate       132617416126243946                                                                                        
  CHROME_CRASHPAD_PIPE_NAME      \\.\pipe\LOCAL\crashpad_13884_LUZUGVEMBFFUOJPK                                                            
  COLORTERM                      truecolor                                                                                                 
  CommonProgramFiles             C:\Program Files\Common Files                                                                             
  CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files                                                                       
  CommonProgramW6432             C:\Program Files\Common Files                                                                             
  COMPUTERNAME                   LAPTOP-QC65VLHJ                                                                                           
  ComSpec                        C:\WINDOWS\system32\cmd.exe                                                                               
  DriverData                     C:\Windows\System32\Drivers\DriverData                                                                    
  GIT_ASKPASS                    c:\Users\Matthias\AppData\Local\Programs\Microsoft VS Code\resources\app\extensions\git\dist\askpass.sh   
  HOMEDRIVE                      C:                                                                                                        
  HOMEPATH                       \Users\Matthias                                                                                           
  LANG                           en_US.UTF-8                                                                                               
  LOCALAPPDATA                   C:\Users\Matthias\AppData\Local                                                                           
  LOGONSERVER                    \\LAPTOP-QC65VLHJ                                                                                         
  NUMBER_OF_PROCESSORS           8                                                                                                         
  OneDrive                       C:\Users\Matthias\OneDrive                                                                                
  OneDriveConsumer               C:\Users\Matthias\OneDrive                                                                                
  ORIGINAL_XDG_CURRENT_DESKTOP   undefined                                                                                                 
  OS                             Windows_NT                                                                                                
  Path                           C:\Program Files (x86)\VMware\VMware Workstation\bin\;C:\Program Files (x86)\Common Files\Oracle\Java\j...
  PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL                                                
  POWERSHELL_DISTRIBUTION_CHA... PSES                                                                                                      
  PROCESSOR_ARCHITECTURE         AMD64                                                                                                     
  PROCESSOR_IDENTIFIER           AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD                                                         
  PROCESSOR_LEVEL                23                                                                                                        
  PROCESSOR_REVISION             6001                                                                                                      
  ProgramData                    C:\ProgramData                                                                                            
  ProgramFiles                   C:\Program Files                                                                                          
  ProgramFiles(x86)              C:\Program Files (x86)                                                                                    
  ProgramW6432                   C:\Program Files                                                                                          
  PSExecutionPolicyPreference    Unrestricted                                                                                              
  PSModulePath                   C:\Users\Matthias\Documents\WindowsPowerShell\Modules;C:\Program Files\WindowsPowerShell\Modules;C:\WIN...
  PUBLIC                         C:\Users\Public                                                                                           
  SESSIONNAME                    Console                                                                                                   
  SystemDrive                    C:                                                                                                        
  SystemRoot                     C:\WINDOWS                                                                                                
  TEMP                           C:\Users\Matthias\AppData\Local\Temp                                                                      
  TERM_PROGRAM                   vscode                                                                                                    
  TERM_PROGRAM_VERSION           1.75.1                                                                                                    
  TMP                            C:\Users\Matthias\AppData\Local\Temp                                                                      
  USERDOMAIN                     LAPTOP-QC65VLHJ                                                                                           
  USERDOMAIN_ROAMINGPROFILE      LAPTOP-QC65VLHJ                                                                                           
  USERNAME                       Matthias                                                                                                  
  USERPROFILE                    C:\Users\Matthias                                                                                         
  VSCODE_GIT_ASKPASS_EXTRA_ARGS  --ms-enable-electron-run-as-node                                                                          
  VSCODE_GIT_ASKPASS_MAIN        c:\Users\Matthias\AppData\Local\Programs\Microsoft VS Code\resources\app\extensions\git\dist\askpass-ma...
  VSCODE_GIT_ASKPASS_NODE        C:\Users\Matthias\AppData\Local\Programs\Microsoft VS Code\Code.exe                                       
  VSCODE_GIT_IPC_HANDLE          \\.\pipe\vscode-git-36e378f399-sock                                                                       
  windir                         C:\WINDOWS                                                                                                



  ```

* Vous remarquez donc que les différentes variables peuvent être listées avec `Get-ChildItem env:` ou `Get-ChildItem variable:`
  > Oui
* La cmd-let `Test-Path` permet de tester l’existence d’un chemin. Essayez-la sur une variable existante, par exemple **mesInterfaces**. Supprimez la variable et retestez ensuite.

  ```powershell
  Test-Path Variable:\mesInterfaces

  Remove-Item Variable:\mesInterfaces

  Test-Path Variable:mesInterfaces

  ```

  **Résultat**

  ```txt
  True
  False
  ```

* Toujours en vous appuyant sur l’aide (get-help variable par exemple), retrouvez les différentes `cmd-lets` vous permettant d’effectuer des actions sur les variables.

  ```powershell
  Get-Help variable
  ```

  **Résultat**

  ```txt
  Name                              Category  Module                    Synopsis
  ----                              --------  ------                    --------
  Clear-Variable                    Cmdlet    Microsoft.PowerShell.U... ...
  Get-Variable                      Cmdlet    Microsoft.PowerShell.U... ...
  New-Variable                      Cmdlet    Microsoft.PowerShell.U... ...
  Remove-Variable                   Cmdlet    Microsoft.PowerShell.U... ...
  Set-Variable                      Cmdlet    Microsoft.PowerShell.U... ...
  Set-DynamicParameterVariables     Function  Pester                    ...
  ```

> Vous avez dû remarquer la convention de nommage très pratique des `cmd-lets : VERBE-NOM`

# 4. Manipulation des processus

* Lancez l’application notepad depuis votre terminal Powershell.

  ```powershell
  notepad.exe
  ```

* Utilisez la cmd-let `get-process` pour identifier l’identifiant du processus qui exécute notepad.

  ```powershell
  Get-Process notepad
  ```

  **Résultat**

  ```txt
  Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
  -------  ------    -----      -----     ------     --  -- -----------
      244      13     3092      14536       0,06   7372   4 notepad
  ```

* Utilisez la cmd-let `Stop-Process` pour terminer le processus notepad. Refaites de même mais en utilisant l'option –confirm à la cmd-let `Stop-Process`.

  ```powershell
  Stop-Process 7372 -Confirm
  ```

  ****Résultat**

  ```txt
  Confirmer
  Êtes-vous sûr de vouloir effectuer cette action ?
  Opération « Stop-Process » en cours sur la cible « notepad (2952) ».
  [O] Oui  [T] Oui pour tout  [N] Non  [U] Non pour tout  [S] Suspendre  [?] Aide (la valeur par défaut est « O ») :
  ```

# 5. Manipulation des services

* Trouvez la commande afin de lister les services.

  ```powershell
  Get-Service
  ```

  **Résultat**

  ```txt
  Status   Name               DisplayName                           
  ------   ----               -----------                           
  Stopped  AarSvc_16e71e9     Agent Activation Runtime_16e71e9      
  Running  AdobeARMservice    Adobe Acrobat Update Service          
  Stopped  AJRouter           Service de routeur AllJoyn            
  Stopped  ALG                Service de la passerelle de la couc...
  Running  AMD External Ev... AMD External Events Utility           
  Stopped  AppIDSvc           Identité de l’application             
  Running  Appinfo            Informations d’application            
  Stopped  AppReadiness       Préparation des applications          
  Stopped  AppXSvc            Service de déploiement AppX (AppXSVC) 
  Running  AsusAppService     ASUS App Service                      
  Running  ASUSLinkNear       ASUS Link Near                        
  Running  ASUSLinkRemote     ASUS Link Remote                      
  Running  ASUSOptimization   ASUS Optimization                     

  ```

* Trouvez ensuite le service qui gère votre imprimante (recherchez 'impression' dans le champ commentaire de la commande précédente). Faites avec un autre service sur les machines de l'IUT.

  ```powershell
  Get-Service -DisplayName *impression*
  ```

* Stoppez, puis relancez votre service d'impression.

  ```powershell
  Stop-Service Spooler
  Start-Service Spooler
  ```

# 6. Exercice 1 : PowerShell est un langage OBJET

`Powershell` exploite et manipule des objets. Un objet est caractérisé par ses **propriétés** (attributs) et ses **méthodes** (actions qu’il peut faire). Les résultats des `cmd-lets` sont également des objets.
Tout est-il vraiment objet ? Oui ! Beaucoup de langages différencient les variables associées à un type de base (int, float, char, array, etc.) et les variables correspondant à des instances d’objets. Avec `Powershell` c’est plus simple tout est objet.

* Définissez deux variables (par exemple `$nom` et `$age` contenant votre prénom et votre age) et étudiez leur type à l’aide de la méthode `Get-Type`.

  ```powershell
  $age = 20
  $nom = "Matthias"

  Write-Output $nom.GetType().Name $age.GetType().Name
  ```

  **Résultat**

  ```txt
  String
  Int32
  ```

> Le simple fait de disposer de méthodes applicables à vos variables vous indique qu'il s'agit d’un objet.

* Listez les propriétés puis les méthodes associées à vos variables.

  ```powershell
  $nom | Get-Member
  ```

  **Résultat**

  ```txt
  Name             MemberType            Definition
  ----             ----------            ----------
  Clone            Method                System.Object Clone(), System.Object ICloneable.Clone()
  CompareTo        Method                int CompareTo(System.Object value), int CompareTo(string strB), int IComparable.CompareTo(Syste...
  Contains         Method                bool Contains(string value)
  CopyTo           Method                void CopyTo(int sourceIndex, char[] destination, int destinationIndex, int count)
  EndsWith         Method                bool EndsWith(string value), bool EndsWith(string value, System.StringComparison comparisonType... 
  Equals           Method                bool Equals(System.Object obj), bool Equals(string value), bool Equals(string value, System.Str... 
  GetEnumerator    Method                System.CharEnumerator GetEnumerator(), System.Collections.IEnumerator IEnumerable.GetEnumerator... 
  GetHashCode      Method                int GetHashCode()
  GetType          Method                type GetType()
  GetTypeCode      Method                System.TypeCode GetTypeCode(), System.TypeCode IConvertible.GetTypeCode()
  IndexOf          Method                int IndexOf(char value), int IndexOf(char value, int startIndex), int IndexOf(string value), in... 
  IndexOfAny       Method                int IndexOfAny(char[] anyOf), int IndexOfAny(char[] anyOf, int startIndex), int IndexOfAny(char... 
  Insert           Method                string Insert(int startIndex, string value)
  IsNormalized     Method                bool IsNormalized(), bool IsNormalized(System.Text.NormalizationForm normalizationForm)
  LastIndexOf      Method                int LastIndexOf(char value), int LastIndexOf(char value, int startIndex), int LastIndexOf(strin... 
  LastIndexOfAny   Method                int LastIndexOfAny(char[] anyOf), int LastIndexOfAny(char[] anyOf, int startIndex), int LastInd... 
  Normalize        Method                string Normalize(), string Normalize(System.Text.NormalizationForm normalizationForm)
  PadLeft          Method                string PadLeft(int totalWidth), string PadLeft(int totalWidth, char paddingChar)
  PadRight         Method                string PadRight(int totalWidth), string PadRight(int totalWidth, char paddingChar)
  Remove           Method                string Remove(int startIndex, int count), string Remove(int startIndex)
  Replace          Method                string Replace(char oldChar, char newChar), string Replace(string oldValue, string newValue)       
  Split            Method                string[] Split(Params char[] separator), string[] Split(char[] separator, int count), string[] ... 
  StartsWith       Method                bool StartsWith(string value), bool StartsWith(string value, System.StringComparison comparison... 
  Substring        Method                string Substring(int startIndex), string Substring(int startIndex, int length)
  ToBoolean        Method                bool IConvertible.ToBoolean(System.IFormatProvider provider)
  ToByte           Method                byte IConvertible.ToByte(System.IFormatProvider provider)
  ToChar           Method                char IConvertible.ToChar(System.IFormatProvider provider)
  ToCharArray      Method                char[] ToCharArray(), char[] ToCharArray(int startIndex, int length)
  ToDateTime       Method                datetime IConvertible.ToDateTime(System.IFormatProvider provider)
  ToDecimal        Method                decimal IConvertible.ToDecimal(System.IFormatProvider provider)
  ToDouble         Method                double IConvertible.ToDouble(System.IFormatProvider provider)
  ToInt16          Method                int16 IConvertible.ToInt16(System.IFormatProvider provider)
  ToInt32          Method                int IConvertible.ToInt32(System.IFormatProvider provider)
  ToInt64          Method                long IConvertible.ToInt64(System.IFormatProvider provider)
  ToLower          Method                string ToLower(), string ToLower(cultureinfo culture)
  ToLowerInvariant Method                string ToLowerInvariant()
  ToSByte          Method                sbyte IConvertible.ToSByte(System.IFormatProvider provider)
  ToSingle         Method                float IConvertible.ToSingle(System.IFormatProvider provider)
  ToString         Method                string ToString(), string ToString(System.IFormatProvider provider), string IConvertible.ToStri... 
  ToType           Method                System.Object IConvertible.ToType(type conversionType, System.IFormatProvider provider)
  ToUInt16         Method                uint16 IConvertible.ToUInt16(System.IFormatProvider provider)
  ToUInt32         Method                uint32 IConvertible.ToUInt32(System.IFormatProvider provider)
  ToUInt64         Method                uint64 IConvertible.ToUInt64(System.IFormatProvider provider)
  ToUpper          Method                string ToUpper(), string ToUpper(cultureinfo culture)
  ToUpperInvariant Method                string ToUpperInvariant()
  Trim             Method                string Trim(Params char[] trimChars), string Trim()
  TrimEnd          Method                string TrimEnd(Params char[] trimChars)
  TrimStart        Method                string TrimStart(Params char[] trimChars)
  Chars            ParameterizedProperty char Chars(int index) {get;}
  Length           Property              int Length {get;}
  ```

  ```powershell
  $age | Get-Member
  ```

  **Résultat**

  ```txt
    Name        MemberType Definition                                                                                                        
  ----        ---------- ----------                                                                                                        
  CompareTo   Method     int CompareTo(System.Object value), int CompareTo(int value), int IComparable.CompareTo(System.Object obj), int...
  Equals      Method     bool Equals(System.Object obj), bool Equals(int obj), bool IEquatable[int].Equals(int other)                      
  GetHashCode Method     int GetHashCode()                                                                                                 
  GetType     Method     type GetType()                                                                                                    
  GetTypeCode Method     System.TypeCode GetTypeCode(), System.TypeCode IConvertible.GetTypeCode()                                         
  ToBoolean   Method     bool IConvertible.ToBoolean(System.IFormatProvider provider)                                                      
  ToByte      Method     byte IConvertible.ToByte(System.IFormatProvider provider)                                                         
  ToChar      Method     char IConvertible.ToChar(System.IFormatProvider provider)                                                         
  ToDateTime  Method     datetime IConvertible.ToDateTime(System.IFormatProvider provider)                                                 
  ToDecimal   Method     decimal IConvertible.ToDecimal(System.IFormatProvider provider)                                                   
  ToDouble    Method     double IConvertible.ToDouble(System.IFormatProvider provider)                                                     
  ToInt16     Method     int16 IConvertible.ToInt16(System.IFormatProvider provider)                                                       
  ToInt32     Method     int IConvertible.ToInt32(System.IFormatProvider provider)                                                         
  ToInt64     Method     long IConvertible.ToInt64(System.IFormatProvider provider)                                                        
  ToSByte     Method     sbyte IConvertible.ToSByte(System.IFormatProvider provider)                                                       
  ToSingle    Method     float IConvertible.ToSingle(System.IFormatProvider provider)                                                      
  ToString    Method     string ToString(), string ToString(string format), string ToString(System.IFormatProvider provider), string ToS...
  ToType      Method     System.Object IConvertible.ToType(type conversionType, System.IFormatProvider provider)                           
  ToUInt16    Method     uint16 IConvertible.ToUInt16(System.IFormatProvider provider)                                                     
  ToUInt32    Method     uint32 IConvertible.ToUInt32(System.IFormatProvider provider)                                                     
  ToUInt64    Method     uint64 IConvertible.ToUInt64(System.IFormatProvider provider)                                                     

  ```

* Identifiez les différences de propriétés et de méthodes, puisque le type de vos variables sont différentes.

  > Voici les méthodes et propriétés qui apparaissent dans le type String mais pas dans le type Int32

  ```txt
  Clone Method
  Contains Method
  CopyTo Method
  EndsWith Method
  GetEnumerator Method
  IndexOf Method
  IndexOfAny Method
  Insert Method
  IsNormalized Method
  LastIndexOf Method
  LastIndexOfAny Method
  Normalize Method
  PadLeft Method
  PadRight Method
  Remove Method
  Replace Method
  Split Method
  StartsWith Method
  Substring Method
  ToCharArray Method
  ToLower Method
  ToLowerInvariant Method
  ToUpper Method
  ToUpperInvariant Method
  Trim Method
  TrimEnd Method
  TrimStart Method
  Chars ParameterizedProperty
  Length Property

  ```

* Définissez une nouvelle variable mais cette fois-ci en utilisant la `cmd-let` dédiée afin de spécifier une valeur et une description. Votre variable devra être en lecture seulement. Remarque : on ne peut pas spécifier le type avec New-Variable.

  ```PowerShell
  Set-Variable testVariable "test" -Description "desc" -Option ReadOnly
  ```

  **Résultat**

  ```txt
  PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts> get-variable testVariable | Select * 
  
  Name        : testVariable
  Description : desc
  Value       : test
  Visibility  : Public
  Module      :
  ModuleName  :
  Options     : ReadOnly
  Attributes  : {}
  ```

# 7. Exercice 2 : Objets utiles

La variable `$host` est un objet instance de la classe `System.Management.Automation.Host.PSHost` recensant des informations sur le système utilisé.

* Consultez les propriétés de cet objet et les méthodes en utilisant le pipe `|` et la `cmd-let Get-Member`,

  ```powershell
  $host | Get-Member
  ```

  **Résultat**

  ```txt
  Name                   MemberType Definition                                                                                             
  ----                   ---------- ----------                                                                                             
  EnterNestedPrompt      Method     void EnterNestedPrompt()                                                                               
  Equals                 Method     bool Equals(System.Object obj)                                                                         
  ExitNestedPrompt       Method     void ExitNestedPrompt()                                                                                
  GetHashCode            Method     int GetHashCode()                                                                                      
  GetType                Method     type GetType()                                                                                         
  NotifyBeginApplication Method     void NotifyBeginApplication()                                                                          
  NotifyEndApplication   Method     void NotifyEndApplication()                                                                            
  PopRunspace            Method     void PopRunspace(), void IHostSupportsInteractiveSession.PopRunspace()                                 
  PushRunspace           Method     void PushRunspace(runspace runspace), void IHostSupportsInteractiveSession.PushRunspace(runspace run...
  SetShouldExit          Method     void SetShouldExit(int exitCode)                                                                       
  ToString               Method     string ToString()                                                                                      
  CurrentCulture         Property   cultureinfo CurrentCulture {get;}                                                                      
  CurrentUICulture       Property   cultureinfo CurrentUICulture {get;}                                                                    
  DebuggerEnabled        Property   bool DebuggerEnabled {get;set;}                                                                        
  InstanceId             Property   guid InstanceId {get;}                                                                                 
  IsRunspacePushed       Property   bool IsRunspacePushed {get;}                                                                           
  Name                   Property   string Name {get;}                                                                                     
  PrivateData            Property   psobject PrivateData {get;}                                                                            
  Runspace               Property   runspace Runspace {get;}                                                                               
  UI                     Property   System.Management.Automation.Host.PSHostUserInterface UI {get;}                                        
  Version                Property   version Version {get;}                                                                                 
  ```

* Affichez maintenant uniquement les propriétés.

  ```powershell
  $host | Get-Member -MemberType Property
  ```

  **Résultat**

  ```txt
  PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts> $host | Get-Member -MemberType Property
   TypeName : System.Management.Automation.Internal.Host.InternalHost
  Name             MemberType Definition
  ----             ---------- ----------
  CurrentCulture   Property   cultureinfo CurrentCulture {get;}
  CurrentUICulture Property   cultureinfo CurrentUICulture {get;}
  DebuggerEnabled  Property   bool DebuggerEnabled {get;set;}
  InstanceId       Property   guid InstanceId {get;}
  IsRunspacePushed Property   bool IsRunspacePushed {get;}
  Name             Property   string Name {get;}
  PrivateData      Property   psobject PrivateData {get;}
  Runspace         Property   runspace Runspace {get;}
  UI               Property   System.Management.Automation.Host.PSHostUserInterface UI {get;}
  Version          Property   version Version {get;}
  ```

* L’objet `System.Management.Automation.Host.PSHost` possède une propriété `ui`, qui est une instance d’objet de
la classe `System.Management.Automation.Host.PSHostUserInterface` qui propose notamment des méthodes d'interaction avec l’interface de commande `Powershell`.
Trouvez quelle méthode de cet objet vous permet de récupérer une ligne saisie au clavier par l’utilisateur.

  ```powershell
  $host.ui.ReadLine()
  ```

* Testez cette méthode en stockant le texte saisi dans une variable que vous afficherez ensuite.

  ```powershell
  $saisie = $host.ui.ReadLine()
  ```

  **Résultat**

  ```txt
  PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts> $saisie = $host.ui.ReadLine()

  test

  PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts>   Get-Variable saisie

  Name                           Value
  ----                           -----
  saisie                         test

  ```

* Il existe des `cmd-let` qui utilise directement les méthodes découvertes précédemment. Il s’agit de `Read-Host` et
de `Write-Host`, et c'est ces commandes que vous utiliserez ensuite.
* Dans le même esprit … Utilisez l’aide de `Powershell` pour découvrir les objets manipulés dans le script cidessous et comprendre ce qu’il fait, même si c’est plutôt explicite :

```powershell
$yes = ([System.Management.Automation.Host.ChoiceDescription]"&oui")
$no = ([System.Management.Automation.Host.ChoiceDescription]"&non")
$selection = [System.Management.Automation.Host.ChoiceDescription[]] ($yes,$no)
$answer = $host.ui.PromptForChoice('Powershell', 'Alors, convaincu par Powershell ?', $selection, 1)
#$selection[$answer]
if ($answer -eq 0) { "C’est vrai que c’est un outil très puissant !!!" }
else { "Tant pis !!!" }
```

**Explication du programme si dessus**

```txt
  On créé deux réponses possibles : Oui ou Non ($yes, $no)
  On créer un choix et et on donne le réponses possibles
  On Créer un prompte avec: 
    titre : Power
    Message: Alors, convaicu par Powershell ?
    le choix créé ($selection)
    la valeur par défaut dans la selection (l'index)
  
  On Met la valeur du prompte dans la variable $answer
  Si la valeur de answer est oui (index 0) on affiche le texte "C'est vrai ..." sinon "Tant pis !!!"
```

# 8. Exercice 3 : Manipulation d'objets

Sous Unix, nous avons vu que le pipe `|` permettait de transférer les résultats d’une commande vers une autre. Ce flux n'était cependant composé que de caractères.

Avec `Powershell`, ce sont des objets qui sont transmis. L’exemple suivant permet de récupérer la liste des services disponibles sur le système par l’intermédiaire de la cmd-let `Get-Service` puis de transmettre chaque objet service à l’instruction `Where-Object` qui applique une contrainte sur la propriété `Status`.

La variable particulière `$_` permet de référencer l’objet actuellement transmis.

```powershell
Get-Service | Where-Object { $_.Status -eq "Running" }
```

* Utilisez ce mécanisme pour afficher les 3 processus les plus anciens.

  ```powershell
  Get-Process | sort-object -property StartTime -descending | select Name, StartTime -First 5
  ```

  **Résultat**

  ```txt
  Name      StartTime
  ----      ---------
  dllhost   28/02/2023 14:23:30
  taskhostw 28/02/2023 14:12:33
  Code      28/02/2023 13:58:18
  Code      28/02/2023 13:58:18
  Code      28/02/2023 13:55:27
  ```

* `WMI` pour `Windows Management Instrumentation` est un système normalisé de gestion du système. Par l'intermédiaire d’objets WMI les scripts peuvent communiquer avec le système.
  * En vous appuyant sur la documentation de la cmd-let `Get-WmiObject`, vous allez afficher la liste des services win32.
  * Ce résultat sera ensuite transmis à l’aide d’un tube à l’itération `ForEach-Object` pour n’afficher que les services lancés.
  * Pour chacun des services win32 lancés vous afficherez son statut, son nom et sa description.

```powershell
Running UnistoreSvc_9502a Gère le stockage ...
Running UserDataSvc_9502a Fournit l’accès des applications ...
Running WpnUserService_9502a Ce service héberge la plate...
```

```powershell

Get-WmiObject -Class Win32_Service | ForEach-Object {
    Write-Output $($_.State + " " + $_.Name + " " + $_.Description)
}

```

**Résultat**

```txt
Running AdobeARMservice Adobe Acrobat Updater keeps your Adobe software up to date.
Stopped AJRouter Achemine les messages AllJoyn pour les clients AllJoyn locaux. Si ce service est arrêté, les clients AllJoyn ne possédant pas leur propre routeur groupé ne peuvent pas s'exécuter.
Stopped ALG Fournit la prise en charge de plug-ins de protocole tiers pour le partage de connexion Internet
Running AMD External Events Utility 
Stopped AppIDSvc Détermine et vérifie l’identité d’une application. La désactivation de ce service empêchera l’application d’AppLocker.
Running Appinfo Permet d’exécuter les applications interactives avec des droits d’administration supplémentaires. Si ce service est arrêté, les utilisateurs ne pourront pas lancer les applications avec les droits d’administration supplémentaires nécessaires pour effectuer les tâches utilisateur souhaitées.
Stopped AppReadiness Prépare les applications pour la première connexion d’un utilisateur sur cet ordinateur et lors de l’ajout de nouvelles applications.

```

**Valid 1 : Faire valider à l'enseignant encadrant l'affichage de vos processus**

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

***

![Creative Commons](images/88x31.png)

[Ce document est mis à disposition selon les termes de la Licence Creative Commons Attribution - Pas d'Utilisation Commerciale - Pas de Modification 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/)

 IUT Lannion © 2023 by R&T is licensed under CC BY-NC-ND 4.0
