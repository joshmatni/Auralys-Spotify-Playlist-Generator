import React from 'react';
import { JsonLdProps } from './jsonld';
export interface LogoJsonLdProps extends JsonLdProps {
    logo: string;
    url: string;
}
declare function LogoJsonLd({ type, keyOverride, ...rest }: LogoJsonLdProps): React.JSX.Element;
export default LogoJsonLd;
