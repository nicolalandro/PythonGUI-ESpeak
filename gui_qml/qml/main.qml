import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Window 2.2
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.0

ApplicationWindow {
    title: qsTr("Test")
    width: 640
    height: 480
    visible: true

    RowLayout {
        id: columnLayout
        anchors.fill: parent
        spacing: 0

        ColumnLayout {
            Layout.preferredWidth: parent.width / 2
            Layout.fillHeight: true

            Text {
                id: element1
                text: qsTr("Voice")
                font.pixelSize: 12
            }
            ColumnLayout{
                RadioButton {
                    id: radioButton
                    text: qsTr("simple google tts")
                    checked: true
                }

                RadioButton {
                    id: radioButton1
                    text: qsTr("espeach")
                }
            }

            Text {
                id: element2
                text: qsTr("Language")
                font.pixelSize: 12
            }
            ColumnLayout{
                RadioButton {
                    id: radioButton2
                    text: qsTr("it")
                    checked: false
                }

                RadioButton {
                    id: radioButton3
                    text: qsTr("en")
                }

                RadioButton {
                    id: radioButton4
                    text: qsTr("es")
                }
            }
            Rectangle{
                id: fill
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
        }
        ColumnLayout {
            Layout.preferredWidth: parent.width / 2
            Layout.fillHeight: true

            Text {
                id: element
                text: qsTr("Write your text")
                font.pixelSize: 12
            }

            ScrollView {
                id: scrollView
                Layout.fillHeight: true
                Layout.fillWidth: true

                TextArea {
                    id: textArea
                    text: qsTr("Text Area")
                    anchors.fill: parent
                }

            }

        }

    }
}





/*##^## Designer {
    D{i:20;anchors_x:0;anchors_y:"-258"}
}
 ##^##*/
