<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>Student Mark Statement</title>
                <style>
                    table {
                        width: 100%;
                        border-collapse: collapse;
                    }
                    th, td {
                        border: 1px solid black;
                        padding: 8px;
                        text-align: center;
                    }
                    th {
                        background-color: #f2f2f2;
                    }
                    .pass {
                        background-color: lightgreen;
                    }
                    .fail {
                        background-color: salmon;
                    }
                </style>
            </head>
            <body>
                <h2>Student Consolidated Mark Statement</h2>
                <table>
                    <tr>
                        <th>Student ID</th>
                        <th>Name</th>
                        <th>AI</th>
                        <th>MWA</th>
                        <th>IS</th>
                        <th>CN</th>
                        <th>BCVS4</th>
                        <th>Total</th>
                        <th>Result</th>
                    </tr>
                    <xsl:for-each select="students/student">
                        <tr>
                            <td><xsl:value-of select="studentID"/></td>
                            <td><xsl:value-of select="name"/></td>

                            
                            <td>
                                <xsl:attribute name="class">
                                    <xsl:choose>
                                        <xsl:when test="AI &gt;= 40">pass</xsl:when>
                                        <xsl:otherwise>fail</xsl:otherwise>
                                    </xsl:choose>
                                </xsl:attribute>
                                <xsl:value-of select="AI"/>
                            </td>

                            
                            <td>
                                <xsl:attribute name="class">
                                    <xsl:choose>
                                        <xsl:when test="MWA &gt;= 40">pass</xsl:when>
                                        <xsl:otherwise>fail</xsl:otherwise>
                                    </xsl:choose>
                                </xsl:attribute>
                                <xsl:value-of select="MWA"/>
                            </td>

                            
                            <td>
                                <xsl:attribute name="class">
                                    <xsl:choose>
                                        <xsl:when test="IS &gt;= 40">pass</xsl:when>
                                        <xsl:otherwise>fail</xsl:otherwise>
                                    </xsl:choose>
                                </xsl:attribute>
                                <xsl:value-of select="IS"/>
                            </td>

                            
                            <td>
                                <xsl:attribute name="class">
                                    <xsl:choose>
                                        <xsl:when test="CN &gt;= 40">pass</xsl:when>
                                        <xsl:otherwise>fail</xsl:otherwise>
                                    </xsl:choose>
                                </xsl:attribute>
                                <xsl:value-of select="CN"/>
                            </td>

                            
                            <td>
                                <xsl:attribute name="class">
                                    <xsl:choose>
                                        <xsl:when test="BCVS4 &gt;= 40">pass</xsl:when>
                                        <xsl:otherwise>fail</xsl:otherwise>
                                    </xsl:choose>
                                </xsl:attribute>
                                <xsl:value-of select="BCVS4"/>
                            </td>

                            <!-- Total Marks -->
                            <td><xsl:value-of select="total"/></td>

                            <!-- Overall Result -->
                            <td>
                                <xsl:attribute name="class">
                                    <xsl:choose>
                                        <xsl:when test="result='Pass'">pass</xsl:when>
                                        <xsl:otherwise>fail</xsl:otherwise>
                                    </xsl:choose>
                                </xsl:attribute>
                                <xsl:value-of select="result"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
